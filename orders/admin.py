from django.contrib import admin
from .models import OrdenesCliente,ItemOrdenesCliente

# Register your models here.
class ItemOrdenesInline(admin.TabularInline):
    model = ItemOrdenesCliente
    campos_id = ['ArticuloItemOrden']

@admin.register(OrdenesCliente)
class OrdenesClienteAdmin(admin.ModelAdmin):
    lista_despl = ['IdOrdenCliente','NombreOrdenCliente','ApellidoPaternoOrdenCliente',
                   'ApellidoMaternoOrdenCliente','CorreoElectronicoOrdenCliente','CodigoPostalOrdenCliente',
                   'EntidadFederativaOrdenCliente','LocalidadOrdenCliente','ColoniaOrdenCliente',
                   'DomicilioOrdenCliente','PagoOrdenCliente']
    lista_filtro = ['PagoOrdenCliente','FechaAlta','FechaCambio']

    inlines = [ItemOrdenesInline]
