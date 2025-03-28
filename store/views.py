from django.shortcuts import render,get_object_or_404
from django.db.models import F
from django.db import connection
from cart.form import AddProductForm
from .models import CategoriasArticulos,AlmacenArticuloExistencias,Articulos,ListaPreciosArticulos
import datetime

# Create your views here.
def get_prices(pIdListaPrecio=None,pIdCategoria='',pIdArticulo=None):
    prices = []
    with connection.cursor() as cursor:
        cursor.callproc('sp_ObtenerPrecios',[pIdListaPrecio,pIdCategoria,pIdArticulo])
        result = cursor.fetchall()
    for price in result:
        prices.append({'IdArticulo':price[0],'PrecioArticulo':price[1]})

    return prices

def get_products(month, year):
    # Construir dinámicamente el nombre del campo basado en el mes
    field_name = f'EntradasExistenciasArticulo{month:02}'  # Formato de dos dígitos para el mes

    # Filtrar usando F objects y retornar los productos
    ids_existing_products = AlmacenArticuloExistencias.objects.filter(**{f'{field_name}__gt': F(f'SalidasExistenciasArticulo{month:02}'), 'EjercicioExistenciasArticulo': year}).values_list('IdArticulo',flat=True)
    products = Articulos.objects.filter(IdArticulo__in = ids_existing_products)
    return products

def get_product(idArticulo,month,year,slug):
    products = get_products(month,year)
    listIds = [product.IdArticulo for product in products]
    if idArticulo in listIds:
        product = get_object_or_404(Articulos,
                                    IdArticulo=idArticulo,
                                    SlugArticulo=slug)
        return product
    else:
        return None

def products_list(request, slug=None,id_categoryLike=None):
    category = None
    categories = CategoriasArticulos.objects.all()
    prices = get_prices(pIdListaPrecio=3)
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    products = get_products(month,year)
    searchLike = False

    if id_categoryLike != None:
        products = products.filter(IdCategoria__IdCategoria__icontains=id_categoryLike)
        prices = get_prices(pIdListaPrecio=3)
        searchLike = True

    if slug:
        category = get_object_or_404(CategoriasArticulos,SlugCategoria=slug)
        products = products.filter(IdCategoria=category)
        prices = get_prices(pIdListaPrecio=3,pIdCategoria=category.IdCategoria)


    return render(request, 'store/products/list.html',
                  {'categoria': category,
                  'categorias':categories,
                  'articulos':products,
                  'precios': prices,
                  'busquedaLike':searchLike})

def product_detail(request,IdArticulo_id,slug):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    product = get_product(IdArticulo_id,month,year,slug)
    price = get_prices(pIdListaPrecio=3,pIdCategoria=product.IdCategoria.IdCategoria,pIdArticulo=product.IdArticulo)[0]['PrecioArticulo']
    cart_form = AddProductForm()
    return render(request, 'store/products/details.html',
                  {'articulo':product,
                   'precio' : price,
                   'form_carrito':cart_form})
