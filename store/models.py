from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from website.models import Usuarios

# Create your models here.
class Almacenes(models.Model):
    IdAlmacen = models.CharField(db_index=True,unique=True,max_length=10)
    NombreAlmacen = models.CharField(max_length=50)
    EtiquetaAlmacen = models.CharField(max_length=15) #Leyenda o nombre corto
    SubAlmacen = models.CharField(max_length=10)
    ResponsableAlmacen = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='responsablesAlmacenes',on_delete=models.PROTECT,db_column="ResponsableAlmacen") #Usuario
    SupervisorAlmacen = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='supervisoresAlmacenes',on_delete=models.PROTECT,db_column="SupervisorAlmacen",default = None) #Usuario
    SuperficieAlmacen = models.DecimalField(max_digits=13,decimal_places=2)
    FechaAperturaAlmacen = models.DateField()
    FechaUltimoInventarioAlmacen = models.DateField()
    HoraUltimoInventarioAlmacen = models.TimeField()
    FechaPenultimoInventarioAlmacen = models.DateField()
    HoraPenultimoInventarioAlmacen = models.TimeField()
    IdElementoAlmacen = models.AutoField(primary_key=True)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioAltaAlmacenes',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioCambioAlmacenes',on_delete=models.PROTECT,db_column="UsuarioCambio",blank=True,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        ordering = ('-IdAlmacen',)
        db_table = "almacenes"
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'

    def __str__(self):
        return f'{self.NombreAlmacen} ({self.IdAlmacen})'


class ProductosSAT(models.Model):
    IdProductoSAT = models.IntegerField(db_index=True,unique=True,primary_key=True)
    DescripcionProductoSAT = models.CharField(max_length=256,default='')
    IncluirIVATrasladoProductoSAT = models.CharField(max_length=1,default='O') #Opcional
    IncluirIEPSRTrasladoProductoSAT = models.CharField(max_length=1,default='N') #No
    ComplementoProductoSAT = models.IntegerField(null=True,blank=True)
    IncluidComplementoProductoSAT = models.CharField(max_length=1,default='N') #No
    CondicionMaterialPeligrosoProductoSAT = models.CharField(max_length=1,default='0') #0
    ClaveMaterialPeligrosoProductoSAT = models.CharField(max_length=5,null=True,blank=True)
    ValorSistema = models.CharField(max_length=1,default='S') #Si
    UsuarioAlta = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioAltaProductosSAT',on_delete=models.PROTECT,db_column="UsuarioAlta",default='')
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioCambioProductosSAT',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = "productossat"
        ordering = ('-IdProductoSAT',)
        verbose_name = 'ProductoSAT'
        verbose_name_plural = 'ProductosSAT'

    def __str__(self):
        return f'{self.DescripcionProductoSAT} ({self.IdProductoSAT})'

class UnidadesSAT(models.Model):
    IdUnidadSAT = models.CharField(max_length=3,db_index=True,unique=True,primary_key=True)
    NombreUnidadSAT = models.CharField(max_length=128)
    DescripcionUnidadSAT = models.CharField(max_length=640)
    NotaUnidadSAT = models.CharField(max_length=256)
    SimboloUnidadSAT = models.CharField(max_length=30)
    ValorSistema = models.CharField(max_length=1)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioAltaUnidadesSAT',on_delete=models.PROTECT,db_column="UsuarioAlta",blank=True)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioCambioUnidadesSAT',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "unidadessat"
        ordering = ('-IdUnidadSAT',)
        verbose_name = 'UnidadSAT'
        verbose_name_plural = 'UnidadesSAT'

    def __str__(self):
        return f'{self.NombreUnidadSAT} ({self.IdUnidadSAT})'


class CategoriasArticulos(models.Model):
    IdCategoria = models.CharField(max_length=8,db_index=True,unique=True)
    IdElementoCategoria = models.AutoField(primary_key=True)
    DescripcionCategoria = models.CharField(max_length=50)
    SubCategoria = models.CharField(max_length=8,null=True,blank=True)
    CondicionExistenciaCategoria = models.CharField(max_length=1) #Valida si existe o no en almacen (S/N)
    SlugCategoria = models.SlugField(max_length=200,unique=True,blank=True)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioAltaCategorias',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioCambioCategorias',on_delete=models.PROTECT,db_column="UsuarioCambio",blank=True,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "categoriasarticulos"
        ordering = ('-IdCategoria',)
        verbose_name = 'CategoriaArticulos'
        verbose_name_plural = 'CategoriasArticulos'
        unique_together = (('IdCategoria','SlugCategoria'))

    def save(self,*args,**kwargs):
        if not self.SlugCategoria:
            self.SlugCategoria = slugify(self.DescripcionCategoria)
        super(CategoriasArticulos,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.DescripcionCategoria} ({self.IdCategoria})';

    def get_absolute_url(self):
        return reverse("store:products_list_by_category",args=[self.SlugCategoria])

class Catalogos(models.Model):
    IdCatalogo = models.IntegerField(db_index=True)
    ElementoCatalogo = models.AutoField(primary_key=True,db_index=True,unique=True)
    DescripcionCatalogo = models.CharField(max_length=128,default="")
    ClaseCatalogo = models.CharField(max_length=15, default = "") #Clasifica elementos del catalogo basados en la necesidas de la aplicacion
    PorDefectoCatalogo = models.CharField(max_length=1, default = "N") # Si/No
    ValorSistema = models.CharField(max_length=1, default = "N") #Si/No
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaCatalogos',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioCatalogos',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'catalogos'
        ordering = ('-IdCatalogo',)
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'
        unique_together = (('IdCatalogo','ElementoCatalogo'),)
        index_together = (('IdCatalogo','ElementoCatalogo'),)

    def __str__(self):
        return f'{self.DescripcionCatalogo} ({self.IdCatalogo})'

class Impuestos(models.Model):
    IdImpuesto = models.IntegerField(db_index=True,primary_key=True,unique=True)
    DescripcionImpuesto = models.CharField(max_length=60)
    EtiquetaImpuesto = models.CharField(max_length=15)
    ClaveSHCPImpuesto = models.ForeignKey(Catalogos,to_field='ElementoCatalogo',related_name='clavesSHCPImpuestos',on_delete=models.PROTECT,db_column='ClaveSHCPImpuesto') #032
    ValorSistema = models.CharField(max_length=1,default='N')
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaImpuestos',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioImpuestos',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'impuestos'
        ordering = ('-IdImpuesto',)
        verbose_name = 'Impuesto'
        verbose_name_plural = 'Impuestos'

    def __str__(self):
        return f'{self.DescripcionImpuesto} ({self.IdImpuesto})'

class ImpuestoTasas(models.Model):
    IdImpuesto = models.ForeignKey(Impuestos,to_field='IdImpuesto',related_name='impuestosTasas',on_delete=models.PROTECT,db_column='IdImpuesto',db_index=True)
    IdTasaImpuesto = models.IntegerField(db_index=True,unique=True)
    TasaImpuesto = models.DecimalField(max_digits=11,decimal_places=4) #Porcentaje de impuesto a aplicar
    EtiquetaImpuesto = models.CharField(max_length=15)
    BaseCalculoImpuesto = models.CharField(max_length=1) #A:Importe Acumulado B:Importe Base
    ClaseImpuesto = models.CharField(max_length=1) #R:Retenido (Se resta al total) T:Trasladado(Se suma al total)
    OrdenImpuesto = models.IntegerField() #Determina el orden de aplicacion y presentacion del impuesto
    TipoFactorSATImpuesto = models.CharField(max_length=1) #T:Tasa, C:Cuota, E:Exento
    BaseImpuesto = models.DecimalField(max_digits=22,decimal_places=6,default=0)
    IdElementoTasaImpuesto = models.AutoField(primary_key=True)
    ValorSistema = models.CharField(max_length=1,default='N')
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaImpuestoTasas',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioImpuestoTasas',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'impuestotasas'
        verbose_name = 'ImpuestoTasa'
        verbose_name_plural = 'ImpuestoTasas'
        ordering = ('-IdImpuesto',)
        index_together = (('IdImpuesto','IdTasaImpuesto'),)
        unique_together = (('IdImpuesto','IdTasaImpuesto'),)

    def __str__(self):
        return f'{self.EtiquetaImpuesto} ({self.TasaImpuesto})'

class CondicionesPago(models.Model):
    """Los términos o condiciones de pago se mostrarán como:
    CONTADO
    30 DÍAS DE CRÉDITO
    2% POR PRONTO PAGO Y 10 DÍAS DE CRÉDITO, 30 DÍAS DE CRÉDITO
    COD (Cobrar o devolver)
    PAGAR AL RECIBIR
    CHEQUE POSTFECHADO
    CRÉDITO
    La notación americana representa el crédito comercial como:
    NET 30 DAYS
    2% 10, NET 30 DAYS
    El primero indica que el pago total se espera dentro de los 30 días siguientes a la entrega de la mercancía o servicios.
    El segundo indica que el Comprador puede aplicar un descuento del 2% sobre el pago total si este se realiza dentro de los 10 días siguientes a la entrega de la mercancía o servicio,
    o el pago total si lo realiza dentro de los 30 días.
"""
    IdCondicionPago = models.IntegerField(db_index=True,primary_key=True,unique=True)
    DescripcionCondicionPago = models.CharField(max_length=60)
    DiasCreditoCondicionPago = models.IntegerField() #Si el valor es CEROm defina una condicion de pago de contado
    DescuentoProntoPagoCondicionPago = models.DecimalField(max_digits=7,decimal_places=2) #Aplica a todos los productos siempre y cuando se cumpla la condicion de pronto pago
    DiasProntoPagoCondicionPago = models.IntegerField()  #Dias maximos en los que aplica el descuento de pronto pago mayor a CERO, este plazo debe ser menor que el plazo a credito
    ValorSistema = models.CharField(max_length=1) #S:Si/N:No
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaCondicionesPago',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioCondicionesPago',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'condicionespago'
        ordering = ('-IdCondicionPago',)
        verbose_name = 'CondicionPago'
        verbose_name_plural = 'CondicionesPago'

    def __str__(self):
        return f'{self.DescripcionCondicionPago} ({self.IdCondicionPago})'



class Proveedores(models.Model):
    IdProveedor = models.IntegerField(db_index=True,unique=True)
    RazonSocialProveedor = models.CharField(max_length=128)
    TipoSociedadProveedor = models.ForeignKey(Catalogos,to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='TipoSociedadProveedor',null=True,blank=True) #IdCatalgo = 049
    ApellidoPaternoProveedor = models.CharField(max_length=30)
    ApellidoMaternoProveedor = models.CharField(max_length=30)
    NombreProveedor = models.CharField(max_length=30)
    DenominacionProveedor = models.CharField(max_length=30) #Nombre comercial del proveedor
    TipoProveedor = models.ForeignKey(Catalogos,related_name='tiposProveedores',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='TipoProveedor',null=True,blank=True) #IdCatalogo = 039
    GiroProveedor = models.ForeignKey(Catalogos,related_name='girosProveedores',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='GiroProveedor') #IdCatalogo = 010
    SectorProveedor = models.ForeignKey(Catalogos,related_name='sectoresProveedores',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='SectorProveedor') #IdCatalogo = 009
    ProcedenciaProveedor = models.CharField(max_length=1) #N:Nacional/E:Extranjero/G:Global
    ClaseProveedor = models.CharField(max_length=1) #F:Fisica/M:Moral
    RFCProveedor = models.CharField(max_length=13)
    CURProveedor = models.CharField(max_length=18)
    FechaAltaProveedor = models.DateField()
    FechaBajaProveedor = models.DateField(null=True,blank=True)
    OpinionSATProveedor = models.CharField(max_length=1) #0:Negativa,1:Positiva
    FechaOpinionSATProveedor = models.DateField(null=True,blank=True) #Fecha ultima de revision del cumplimientos de las obligaciones fiscales
    ObservacionesProveedor = models.CharField(max_length=256)
    CondicionPagoProveedor = models.ForeignKey(CondicionesPago,related_name='condicionesPagoProveedores',to_field='IdCondicionPago',on_delete=models.PROTECT,db_column='CondicionPagoProveedor')
    FechaAperturaProveedor = models.DateField(null=True,blank=True) #Fecha de apertura de linea de credito
    LimiteCreditoProveedor = models.DecimalField(max_digits=22,decimal_places=6)
    PorcentajeAnticipoProveedor = models.DecimalField(max_digits=5,decimal_places=2)
    DescuentoProveedor = models.DecimalField(max_digits=15,decimal_places=6) #Descuento Comercial
    PlazoEntrega = models.IntegerField()
    CriterioPagoProveedor = models.CharField(max_length=1)
    DivisaProveedor = models.ForeignKey('Divisas',related_name='divisasProveedores',to_field='IdDivisa',on_delete=models.PROTECT,db_column='DivisaProveedor')
    NumeroCuentaProveedor = models.IntegerField()
    IdElementoProveedor = models.AutoField(primary_key=True)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaProveedores',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioProveedores',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        ordering = ('-IdProveedor',)
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedores'

    def __str__(self):
        return f'{self.DenominacionProveedor} ({self.IdProveedor})'


class Articulos(models.Model):
    IdCategoria = models.ForeignKey(CategoriasArticulos,to_field = 'IdCategoria',related_name="categoriasArticulos",on_delete=models.PROTECT,db_index=True,db_column="IdCategoria")
    IdArticulo = models.IntegerField(db_index=True,unique=True) #SKU (Stock Keeping Unit)
    NombreArticulo = models.CharField(max_length=256)
    EtiquetaArticulo = models.CharField(max_length=15)
    UPCArticulo = models.CharField(max_length=13,null=True,blank=True)
    IdProductoSATArticulo = models.ForeignKey(ProductosSAT,to_field = 'IdProductoSAT',related_name="productosSAT",on_delete=models.PROTECT,db_column="IdProductoSATArticulo")
    DescripcionArticulo = models.CharField(max_length=1026)
    MarcaArticulo = models.ForeignKey('MarcasArticulos',to_field='IdMarca',related_name="marcas",on_delete=models.PROTECT,db_column="MarcaArticulo",null=True,blank=True)
    ModeloArticulo = models.CharField(max_length=40)
    MedidaArticulo = models.CharField(max_length=5)
    UnidadMedidaArticulo = models.ForeignKey(Catalogos,related_name='unidadesMedidasArticulos',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='UnidadMedidaArticulo',null=True,blank=True) #IdCatalogo = 017
    PresentacionArticulo = models.ForeignKey('PresentacionesArticulos',to_field='IdPresentacion',related_name="presentaciones",on_delete=models.PROTECT,db_column="PresentacionArticulo",null=True,blank=True)
    FabricanteArticulo = models.ForeignKey(Catalogos,related_name='fabricantesArticulos',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='FabricanteArticulo',null=True,blank=True) #IdCatalogo = 018
    ClaseArticulo = models.ForeignKey(Catalogos,related_name='clasesArticulos',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='ClaseArticulo',null=True,blank=True) #IdCatalogo = 017
    ProveedorPrimarioArticulo = models.ForeignKey(Proveedores,related_name='proveedoresArticulos',to_field='IdProveedor',on_delete=models.PROTECT,db_column='ProveedorPrimarioArticulo')
    CotizacionesArticulo = models.IntegerField()
    ProcedenciaArticulo = models.CharField(max_length=1) #N:Nacional E:Extranjero
    ArancelArticulo = models.DecimalField(max_digits=7,decimal_places=2)
    MargenArticulo = models.DecimalField(max_digits=11,decimal_places=4)
    UnidadExistenciaArticulo = models.ForeignKey(Catalogos,related_name='unidadesExisteniciasArticulos',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='UnidadExistenciaArticulo') #IdCatalogo = 016
    UnidadesEntradaArticulo = models.ForeignKey(Catalogos,related_name='unidadesEntradasArticulos',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='UnidadesEntradaArticulo') #IdCatalogo = 016
    UnidadesSalidaArticulo = models.ForeignKey(Catalogos,related_name='unidadesSalidasArticulos',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='UnidadesSalidaArticulo') #IdCatalogo = 016
    UnidadEmbalajeArticulo = models.ForeignKey(Catalogos,related_name='unidadesEmbalajesArticulos',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='UnidadEmbalajeArticulo',default='') #IdCatalogo = 016
    IdUnidadSATArticulo = models.ForeignKey(UnidadesSAT,to_field='IdUnidadSAT',related_name="unidadesSAT",on_delete=models.PROTECT,max_length=3,db_column="IdUnidadSATArticulo")
    FactorEntradaArticulo = models.DecimalField(max_digits=16,decimal_places=5)
    FactorSalidaArticulo = models.DecimalField(max_digits=16,decimal_places=5)
    FactorEmbalajeArticulo = models.DecimalField(max_digits=16,decimal_places=5)
    CantidadUnidadesArticulo = models.IntegerField()
    FactorLitrosArticulo = models.DecimalField(max_digits=16,decimal_places=5)
    AnchoArticulo = models.DecimalField(max_digits=10,decimal_places=3)
    AltoArticulo = models.DecimalField(max_digits=10,decimal_places=3)
    FondoArticulo = models.DecimalField(max_digits=10,decimal_places=3)
    PesoArticulo = models.DecimalField(max_digits=14,decimal_places=3)
    ImagenArticulo = models.ImageField(upload_to='productos/%Y/%m/%d', null=True,blank=True)
    FormatoImagenArticulo = models.CharField(max_length=50,null=True,blank=True)
    NombreImagenArticulo = models.CharField(max_length=128,null=True,blank=True)
    CondicionReordenArticulo = models.CharField(max_length=1)
    CondicionFraccionesArticulo = models.CharField(max_length=1)
    CondicionExistenciaNegativaArticulo = models.CharField(max_length=1)
    CondicionEtiquetaArticulo = models.CharField(max_length=1)
    CondicionMantenimientoArticulo = models.CharField(max_length=1)
    CondicionPrecioVentaArticulo = models.CharField(max_length=1)
    CondicionPrecioCompraArticulo = models.CharField(max_length=1)
    Garantia1Articulo = models.IntegerField()
    Garantia2Articulo = models.IntegerField()
    CondicionReemplazoArticulo = models.CharField(max_length=1)
    CaducidadArticulo = models.DateField()
    OperacionSATArticulo = models.ForeignKey(Catalogos,related_name='operacionesSATArticulos',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='OperacionSATArticulo',null=True,blank=True) #IdCatalogo = 041
    IdElementoArticulo = models.AutoField(primary_key=True)
    SlugArticulo = models.SlugField(max_length=200,unique=True,blank=True)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaArticulos',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioArticulos',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = "articulos"
        ordering = (('-IdCategoria'),)
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        unique_together = (('IdCategoria','IdArticulo'),)
        index_together = (('IdCategoria','IdArticulo'),)

    def save(self,*args,**kwargs):
        if not self.SlugArticulo:
            self.SlugArticulo = slugify(self.EtiquetaArticulo)
        super(Articulos,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.NombreArticulo} ({self.IdArticulo})'

    def get_absolute_url(self):
        return reverse("store:product_detail",args=[self.IdArticulo,self.SlugArticulo])

    def getIdArticulo(self):
        return self.IdArticulo

class Divisas(models.Model):
    IdDivisa = models.CharField(max_length=3,db_index=True,unique=True)
    NombreDivisa = models.CharField(max_length=40)
    EtiquetaDivisa = models.CharField(max_length=15) #Nombre Corto (PESOS, DOLARES,ETC)
    SimboloDivisa = models.CharField(max_length=3) #$,etc
    BanderaDivisa = models.ImageField(upload_to='divisas/%Y/%m/%d', null=True,blank=True)
    FormatoBanderaDivisa = models.CharField(max_length=50,null=True,blank=True)
    NombreBanderaDivisa = models.CharField(max_length=128,null=True,blank=True)
    PorDefectoDivisa = models.CharField(max_length=1,default='N')
    ValorSistema = models.CharField(max_length=1,default='S') #Si
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaDivisas',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioDivisas',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'divisas'
        ordering = ('-IdDivisa',)
        verbose_name = 'Divisa'
        verbose_name_plural = 'Divisas'

    def __str__(self):
        return f'{self.NombreDivisa} ({self.IdDivisa})'



class CostosArticulos(models.Model):
    IdCategoria = models.ForeignKey(CategoriasArticulos,related_name="categoriasCostosArticulos",db_column='IdCategoria',on_delete=models.PROTECT,db_index=True)
    IdArticulo = models.ForeignKey(Articulos,related_name="articulosCostosArticulos",db_column="IdArticulo",on_delete=models.PROTECT,db_index=True)
    FechaCosto = models.DateField(db_index=True)
    CostoUnitario = models.DecimalField(max_digits=22,decimal_places=6)
    DivisaCosto = models.ForeignKey(Divisas,related_name="divisasCostosArticulos",on_delete=models.PROTECT,db_column="IdDivisa")
    TipoCambioCosto = models.DecimalField(max_digits=22,decimal_places=6)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaCostosArticulos',on_delete=models.PROTECT,db_column="UsuarioAlta",blank=True)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioCostosArticulos',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = 'costosarticulos'
        verbose_name = 'CostosArticulo'
        verbose_name_plural = 'CostosArticulos'
        index_together = (('IdCategoria','IdArticulo','FechaCosto'),)
        unique_together = (('IdCategoria','IdArticulo','FechaCosto'),)

    def __str__(self):
        return f'{self.IdArticulo} ({self.CostoUnitario})'

class MarcasCategorias(models.Model):
    IdCategoria = models.ForeignKey(CategoriasArticulos,on_delete=models.PROTECT,to_field='IdCategoria',db_column='IdCategoria')
    IdMarca = models.ForeignKey('MarcasArticulos',on_delete=models.PROTECT,to_field='IdMarca',db_column='IdMarca')

    class Meta:
        db_table = 'marcascategorias'


class MarcasArticulos(models.Model):
    IdCategoria = models.ManyToManyField(CategoriasArticulos,through=MarcasCategorias,db_index=True)
    IdMarca = models.IntegerField(db_index=True,unique=True)
    DescripcionMarca = models.CharField(max_length=50)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioAltaMarcasArticulos',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioCambioMarcasArticulos',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "marcasarticulos"
        ordering = ('-IdMarca',)
        verbose_name = "MarcaArticulos"
        verbose_name_plural = "MarcasArticulos"

    def __str__(self):
        return f'{self.DescripcionMarca} ({self.IdMarca})'


class PresentacionesCategorias(models.Model):
    IdCategoria = models.ForeignKey(CategoriasArticulos,on_delete=models.PROTECT,to_field='IdCategoria',db_column='IdCategoria')
    IdPresentacion = models.ForeignKey('PresentacionesArticulos',on_delete=models.PROTECT,to_field='IdPresentacion',db_column='IdPresentacion')

    class Meta:
        db_table = 'presentacionescategorias'


class PresentacionesArticulos(models.Model):
    IdCategoria = models.ManyToManyField(CategoriasArticulos,through=PresentacionesCategorias,db_index=True)
    IdPresentacion = models.IntegerField(db_index=True,unique=True)
    DescripcionPresentacion = models.CharField(max_length=50)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioAltaPresentacionesArticulos',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field = 'IdUsuario',related_name='usuarioCambioPresentacionesArticulos',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "presentacionesarticulos"
        ordering = ('-IdPresentacion',)
        verbose_name = 'PresentacionArticulos'
        verbose_name_plural = 'PresentacionesArticulos'

    def __str__(self):
        return f'{self.DescripcionPresentacion} ({self.IdPresentacion})'

class AlmacenArticulos(models.Model):
    IdAlmacen = models.ForeignKey(Almacenes,to_field='IdAlmacen',related_name="almacenesArticulos",on_delete=models.PROTECT,db_index=True,max_length=10,db_column="IdAlmacen")
    IdCategoria = models.ForeignKey(CategoriasArticulos,to_field='IdCategoria',related_name="categoriasAlmacenArticulos",on_delete=models.PROTECT,db_index=True,max_length=8,db_column="IdCategoria")
    IdArticulo = models.ForeignKey(Articulos,to_field='IdArticulo',related_name="articulosAlmacenArticulos",on_delete=models.PROTECT,db_index=True,max_length=10,db_column="IdArticulo")
    MaximoArticuloAlmacen = models.DecimalField(max_digits=14,decimal_places=3) #Nivel de inventario maximo (Cumplir pedidos y no sobrealmacenar)
    MinimoArtiuloAlmacen = models.DecimalField(max_digits=14,decimal_places=3) #Nivel de inventario minimo (Cantidad minima que se requiere para cubrir pedidos)
    ReordenArticuloAlmacen = models.DecimalField(max_digits=14,decimal_places=3)
    UbicacionArticuloAlmacen = models.CharField(max_length=6)
    ProveedorPrimarioArticuloAlmacen = models.IntegerField(null=True)
    IdElementoProveedor = models.AutoField(primary_key=True)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaAlmacen',on_delete=models.PROTECT,db_column="UsuarioAlta",blank=True)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioAlmacen',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "almacenarticulos"
        ordering = ('-IdAlmacen',)
        verbose_name = 'AlmacenArticulo'
        verbose_name_plural = 'AlmacenArticulos'
        index_together = (('IdAlmacen','IdCategoria','IdArticulo'),)
        unique_together = (('IdAlmacen','IdCategoria','IdArticulo'),)

class AlmacenArticuloExistencias(models.Model):
    IdAlmacen = models.ForeignKey(Almacenes,to_field='IdAlmacen',related_name="almacenesArticuloExistencias",on_delete=models.PROTECT,db_index=True,max_length=10,db_column="IdAlmacen")
    IdCategoria = models.ForeignKey(CategoriasArticulos,to_field='IdCategoria',related_name="categoriasAlmacenArticuloExistencias",on_delete=models.PROTECT,db_index=True,max_length=8,db_column="IdCategoria")
    IdArticulo = models.ForeignKey(Articulos,to_field='IdArticulo',related_name="articulosAlmacenArticuloExistencias",on_delete=models.PROTECT,db_index=True,max_length=10,db_column="IdArticulo")
    IdEstadoExistencia = models.IntegerField(db_index=True)
    EjercicioExistenciasArticulo = models.IntegerField(db_index=True)
    InicialExistenciasArticulo = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo01 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo02 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo03 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo04 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo05 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo06 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo07 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo08 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo09 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo10 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo11 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    EntradasExistenciasArticulo12 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo01 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo02 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo03 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo04 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo05 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo06 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo07 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo08 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo09 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo10 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo11 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    SalidasExistenciasArticulo12 = models.DecimalField(max_digits=16,decimal_places=3,default=0)
    IdElementoAlmacenArticuloExistencia = models.AutoField(primary_key=True)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaExistencias',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioExistencias',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = "almacenarticuloexistencias"
        ordering = ['IdAlmacen','IdCategoria','IdArticulo']
        verbose_name = 'AlmacenArticuloExistencia'
        verbose_name_plural = 'AlmacenArticuloExistencias'
        index_together = (('IdAlmacen','IdCategoria','IdArticulo','IdEstadoExistencia','EjercicioExistenciasArticulo'),)
        unique_together = (('IdAlmacen','IdCategoria','IdArticulo','IdEstadoExistencia','EjercicioExistenciasArticulo'),)

    def __str__(self):
        return f'{self.IdArticulo} ({self.EjercicioExistenciasArticulo})'


class Clientes(models.Model):
    IdCliente = models.IntegerField(db_index=True,unique=True)
    RazonSocialCliente = models.CharField(max_length=128)
    TipoSociedadCliente = models.ForeignKey(Catalogos,to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='TipoSociedadCliente',null=True,blank=True) #IdCatalgo = 049
    ApellidoPaternoCliente = models.CharField(max_length=30)
    ApellidoPaternoCliente = models.CharField(max_length=30)
    NombreCliente = models.CharField(max_length=30)
    DenominacionCliente = models.CharField(max_length=30)
    TipoCliente = models.ForeignKey(Catalogos,related_name='tiposClientes',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='TipoCliente') #IdCatalgo = 024
    GiroCliente = models.ForeignKey(Catalogos,related_name='girosClientes',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='GiroCliente') #IdCatalgo = 010
    SectorCliente = models.ForeignKey(Catalogos,related_name='sectoresClientes',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='SectorCliente') #IdCatalgo = 009
    ProcedenciaCliente = models.CharField(max_length=1) #N:Nacional/E:Extranjero/G:Global
    ClaseCliente = models.CharField(max_length=1) #F:Fisica/M:Moral
    RFCCliente = models.CharField(max_length=13)
    CURPCliente = models.CharField(max_length=18)
    ObservacionesCliente = models.CharField(max_length=256)
    FechaAltaCliente = models.DateField()
    FechaBajaCliente = models.DateField(null=True,blank=True)
    CondicionPagoCliente = models.ForeignKey(CondicionesPago,related_name='condicionesPagoClientes',to_field='IdCondicionPago',on_delete=models.PROTECT,db_column='CondicionPagoCliente')
    FechaAperturaCliente = models.DateField(null=True,blank=True) #Fecha de apertura de linea de credito
    LimiteCreditoCliente = models.DecimalField(max_digits=22,decimal_places=6)
    PorcentajeAnticipoCliente = models.DecimalField(max_digits=5,decimal_places=2)
    DescuentoCliente = models.DecimalField(max_digits=15,decimal_places=6) #Descuento Comercial
    PlazoEntrega = models.IntegerField()
    CriterioPagoCliente = models.CharField(max_length=1)
    DivisaCliente = models.ForeignKey('Divisas',related_name='divisasClientes',to_field='IdDivisa',on_delete=models.PROTECT,db_column='DivisaCliente')
    NumeroCuentaCliente = models.IntegerField()
    IdElementoCliente = models.AutoField(primary_key=True)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaClientes',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioClientes',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'clientes'
        ordering = ('-IdCliente',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.DenominacionCliente} ({self.IdCliente})'

class ListasPrecios(models.Model):
    IdListaPrecio = models.IntegerField(db_index=True,primary_key=True,unique=True)
    DescripcionListaPrecio = models.CharField(max_length=40)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaListasPrecios',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioListasPrecios',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'listasprecios'
        ordering = ('-IdListaPrecio',)
        verbose_name = 'ListaPrecio'
        verbose_name_plural = 'ListasPrecios'
    def __str__(self):
        return f'{self.DescripcionListaPrecio} ({self.IdListaPrecio})'

class ListaPreciosArticulos(models.Model):
    IdListaPrecio = models.ForeignKey(ListasPrecios,to_field='IdListaPrecio',related_name='listasPreciosArticulos',on_delete=models.PROTECT,db_column='IdListaPrecio',db_index=True)
    IdCategoria = models.ForeignKey(CategoriasArticulos,to_field='IdCategoria',related_name='categoriasListasPreciosArticulos',on_delete=models.PROTECT,db_column='IdCategoria',db_index=True)
    IdArticulo = models.ForeignKey(Articulos,to_field='IdArticulo',related_name='articulosListasPreciosArticulos',on_delete=models.PROTECT,db_column='IdArticulo',db_index=True)
    FechaInicioPrecio = models.DateField(db_index=True)
    HoraInicioPrecio = models.TimeField(db_index=True)
    PrecioArticulo = models.DecimalField(max_digits=22,decimal_places=6) #Precio Sin Impuestos
    DivisaPrecioArticulo = models.ForeignKey(Divisas,to_field='IdDivisa',related_name='divisasListasPrecios',on_delete=models.PROTECT,db_column='DivisaPrecioArticulo')
    IdElementoPrecioArticulo = models.AutoField(primary_key=True)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaListaPreciosArticulos',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioListaPreciosArticulos',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'listapreciosarticulos'
        ordering = ('-IdListaPrecio',)
        verbose_name = 'ListaPreciosArticulos'
        verbose_name_plural = 'ListasPreciosArticulos'
        index_together = (('IdListaPrecio','IdCategoria','IdArticulo','FechaInicioPrecio',
                           'HoraInicioPrecio'),)
        unique_together = (('IdListaPrecio','IdCategoria','IdArticulo','FechaInicioPrecio',
                           'HoraInicioPrecio'),)

    def __str__(self):
        return f'{self.IdArticulo} - {self.IdListaPrecio}'


class ListaPreciosArticuloImpuestos(models.Model):
    IdListaPrecio = models.ForeignKey(ListasPrecios,to_field='IdListaPrecio',related_name='listasPreciosArticulosImpuestos',on_delete=models.PROTECT,db_column='IdListaPrecio',db_index=True)
    IdCategoria = models.ForeignKey(CategoriasArticulos,to_field='IdCategoria',related_name='categoriasListasPreciosArticuloImpuestos',on_delete=models.PROTECT,db_column='IdCategoria',db_index=True)
    IdArticulo = models.ForeignKey(Articulos,to_field='IdArticulo',related_name='articulosListasPreciosArticulosImpuestos',on_delete=models.PROTECT,db_column='IdArticulo',db_index=True)
    FechaInicioPrecio = models.DateField(db_index=True)
    HoraInicioPrecio = models.TimeField(db_index=True)
    ZonaImpuestoPrecio = models.ForeignKey(Catalogos,related_name='zonasImpuestosListasPrecios',to_field='ElementoCatalogo',on_delete=models.PROTECT,db_column='ZonaImpuestoPrecio',db_index=True) #IdCatalgo = 011
    TipoImpuestoPrecio = models.ForeignKey(Impuestos,to_field='IdImpuesto',related_name='impuestosListasPrecios',on_delete=models.PROTECT,db_column='TipoImpuestoPrecio',db_index=True)
    TasaImpuestoPrecio = models.ForeignKey(ImpuestoTasas,to_field='IdTasaImpuesto',related_name='impuestosTasasListasPrecios',on_delete=models.PROTECT,db_column='TasaImpuestoPrecio',db_index=True)
    BaseCalculoImpuestoPrecio = models.CharField(max_length=1) #A:Importe Acumulado B:Importe Base
    IdElementoImpuestoPrecio = models.AutoField(primary_key=True)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaListaPreciosArticuloImpuestos',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioListaPreciosArticuloImpuestos',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'listapreciosarticuloImpuestos'
        ordering = ('-IdListaPrecio',)
        verbose_name = 'ListaPreciosArticulosImpuestos'
        verbose_name_plural = 'ListasPreciosArticulosImpuestos'
        index_together = (('IdListaPrecio','IdCategoria','IdArticulo','FechaInicioPrecio',
                           'HoraInicioPrecio'),)
        unique_together = (('IdListaPrecio','IdCategoria','IdArticulo','FechaInicioPrecio',
                           'HoraInicioPrecio'),)

    def __str__(self):
        return f'{self.IdArticulo} - {self.IdListaPrecio}'
