from django.shortcuts import render
from .models import ItemOrdenesCliente
from .form import AddOrderForm
from cart.cart import Cart

# Create your views here.

def add_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                ItemOrdenesCliente.objects.create(OrdenItemOrden=order,ArticuloItemOrden=item['producto'],
                                                  PrecioItemOrden=item['precio'],CantidadItemOrden=item['cantidad'])
                cart.clean_cart()
                return render(request,'orders/created.html',{'orden':order})
    else:
        form = AddOrderForm()
    return render(request,'orders/create.html',{'carrito':cart,'formulario':form})
