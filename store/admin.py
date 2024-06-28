from django.contrib import admin
from .models import Almacenes,CategoriasArticulos,Articulos,AlmacenArticulos
from .models import AlmacenArticuloExistencias,MarcasArticulos,MarcasCategorias,PresentacionesArticulos,PresentacionesCategorias
from .models import Proveedores,CondicionesPago,Divisas
from website.models import Usuarios,Empleados

# Register your models here.

admin.site.register(Almacenes)
admin.site.register(CategoriasArticulos)
admin.site.register(Articulos)
admin.site.register(AlmacenArticulos)
admin.site.register(AlmacenArticuloExistencias)
admin.site.register(MarcasArticulos)
admin.site.register(MarcasCategorias)
admin.site.register(PresentacionesArticulos)
admin.site.register(PresentacionesCategorias)
admin.site.register(Proveedores)
admin.site.register(Divisas)
admin.site.register(CondicionesPago)
admin.site.register(Usuarios)
admin.site.register(Empleados)
