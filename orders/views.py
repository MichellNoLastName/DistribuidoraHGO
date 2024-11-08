from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db import connection
from django.contrib import messages
from .models import ItemOrdenesCliente
from .form import AddOrderForm
from .models import Localidades,Colonias,EntidadesFederativas,Usuarios,ContactoMedios
from cart.cart import Cart
import random

# Create your views here.

def add_order(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        userCliente = Usuarios.objects.get(IdUsuario = request.user)
        emailCliente = ContactoMedios.objects.get(UsuarioContactoMedio = userCliente,TipoMedioContacto=178)
        numeroTelefonicoCliente = ContactoMedios.objects.get(UsuarioContactoMedio = userCliente, TipoMedioContacto = 169)


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
            result = "NOK"
            ordenId = None
            while result != "OK":
                ordenId = random.randint(10**6,10**7)
                with connection.cursor() as cursor:
                    cursor.execute("SELECT fn_ValidarIdOrdenCuenta(%s)",params=[ordenId])
                    result = cursor.fetchone()[0]

            form = AddOrderForm(initial={
                'IdOrdenCliente' : ordenId,
                'UsuarioOrdenCliente' : userCliente,
                'NombreOrdenCliente' : userCliente.NombreUsuario,
                'ApellidoPaternoOrdenCliente' : userCliente.ApellidoPaternoUsuario,
                'ApellidoMaternoOrdenCliente' : userCliente.ApellidoMaternoUsuario,
                'CorreoElectronicoOrdenCliente' : emailCliente.DatoTipoMedioContacto,
                'NumeroTelefonicoOrdenCliente' : numeroTelefonicoCliente.DatoTipoMedioContacto,
                'UsuarioAlta' : userCliente
            })
        return render(request,'orders/create.html',{'carrito':cart,'formulario':form})
    else:
        messages.error(request,'Por favor, es necesario iniciar sesión para continuar con su compra')
        return redirect('cart:cart_detail')

def load_towns(request):
    idEntidadFederativa = request.GET.get('idEntidadFederativa')
    towns = Localidades.objects.filter(IdEntidadFederativa=idEntidadFederativa).order_by('NombreLocalidad').all()
    return JsonResponse(list(towns.values('IdLocalidad','NombreLocalidad')),safe=False)

def load_streets(request):
    idEntidadFederativa = request.GET.get('idEntidadFederativa')
    idLocalidad = request.GET.get('idLocalidad')
    streets = Colonias.objects.filter(IdEntidadFederativa=idEntidadFederativa,IdLocalidad=idLocalidad).order_by('NombreColonia').all()
    return JsonResponse(list(streets.values('IdColonia','NombreColonia')),safe=False)

def load_location(request):
    idCodigoPostal = request.GET.get('idCodigoPostal')
    with connection.cursor() as cursor:
        cursor.execute("SELECT IdEntidadFederativa,IdLocalidad FROM CodigosPostales WHERE IdCodigoPostal = %s",[idCodigoPostal])
        result = cursor.fetchone()

    data = []
    if result is not None:
        idEntidadFederativa,idLocalidad = result
        entidadFederativa = EntidadesFederativas.objects.get(IdEntidadFederativa=idEntidadFederativa)
        localidad = Localidades.objects.get(IdEntidadFederativa = idEntidadFederativa,IdLocalidad=idLocalidad)
        data.append({'IdEntidadFederativa':entidadFederativa.IdEntidadFederativa,'NombreEntidadFederativa':entidadFederativa.NombreEntidadFederativa})
        data.append({'IdLocalidad':localidad.IdLocalidad,'NombreLocalidad':localidad.NombreLocalidad})

    return JsonResponse(data,safe=False)
