from django.contrib import admin
from .models import Almacenes,CategoriasArticulos,Articulos,AlmacenArticulos,AlmacenArticuloExistencias,MarcasArticulos,PresentacionesArticulos

# Register your models here.

admin.site.register(Almacenes)
admin.site.register(CategoriasArticulos)
admin.site.register(Articulos)
admin.site.register(AlmacenArticulos)
admin.site.register(AlmacenArticuloExistencias)
admin.site.register(MarcasArticulos)
admin.site.register(PresentacionesArticulos)
