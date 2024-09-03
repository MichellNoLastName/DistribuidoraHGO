from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from store.models import Articulos
from .cart import Cart
from .form import AddProductForm

# Create your views here.

@require_POST
def add_cart(request,product_id):
    cart = Cart(request)
    print(request.POST.get('action'))
    product_in = get_object_or_404(Articulos,IdArticulo=product_id)
    if request.POST.get('action') == 'buy': #Comprar
        form = AddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product_in,quantity=cd['quantity'],
                    change_quantity=cd['override'])
        else:
            cart.add(product=product_in,quantity=1,
                    change_quantity=False)

        return redirect('cart:cart_detail')

    elif request.POST.get('action') == 'add': #Agregar Carrito
        form = AddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product_in,quantity=cd['quantity'],
                    change_quantity=cd['override'])
            return redirect('cart:cart_detail')
        else:
            cart.add(product=product_in,quantity=1,
                    change_quantity=False)
        return redirect('store:products_list')


@require_POST
def remove_cart(request,product_id):
    cart = Cart(request)
    product_in = get_object_or_404(Articulos,IdArticulo=product_id)
    cart.remove(product=product_in)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['form_refresh'] = AddProductForm(
            initial={
                'quantity':item['cantidad'],
                'override':True
            }
        )
    return render(request,'cart/detail.html',{'carrito':cart})
