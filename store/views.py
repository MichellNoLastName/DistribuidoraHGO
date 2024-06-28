from django.shortcuts import render,get_object_or_404
from django.db.models import F
from .models import CategoriasArticulos,AlmacenArticuloExistencias,Articulos
import datetime

# Create your views here.
def get_products(month, year):
    # Construir dinámicamente el nombre del campo basado en el mes
    field_name = f'EntradasExistenciasArticulo{month:02}'  # Formato de dos dígitos para el mes

    # Filtrar usando F objects y retornar los productos
    return AlmacenArticuloExistencias.objects.filter(**{f'{field_name}__gt': F(f'SalidasExistenciasArticulo{month:02}'), 'EjercicioExistenciasArticulo': year})

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

def products_list(request, slug=None):
    category = None
    categories = CategoriasArticulos.objects.all()
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    products = get_products(month,year)

    if slug:
        category = get_object_or_404(CategoriasArticulos,SlugCategoria=slug)
        products = products.filter(IdCategoria=category)

    return render(request, 'store/products/list.html',
                  {'categoria': category,
                  'categorias':categories,
                  'articulos':products})

def product_detail(request,idArticulo,slug):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    product = get_product(idArticulo,month,year,slug)
    return render(request, 'store/products/details.html',
                  {'articulo':product})
