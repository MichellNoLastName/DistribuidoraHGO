from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import timezone

# Create your models here.
class Almacenes(models.Model):
    IdAlmacen = models.CharField(db_index=True,unique=True,max_length=10,null=False)
    NombreAlmacen = models.CharField(max_length=50)
    EtiquetaAlmacen = models.CharField(max_length=15) #Leyenda o nombre corto
    SubAlmacen = models.CharField(max_length=10)
    ResponsableAlmacen = models.CharField(max_length=10) #Usuario
    SupervisorAlmacen = models.CharField(max_length=10,null=True) #Usuario
    SuperficieAlmacen = models.DecimalField(max_digits=13,decimal_places=2)
    FechaAperturaAlmacen = models.DateField()
    FechaUltimoInventarioAlmacen = models.DateField()
    HoraUltimoInventarioAlmacen = models.TimeField()
    FechaPenultimoInventarioAlmacen = models.DateField()
    HoraPenultimoInventarioAlmacen = models.TimeField()
    IdElementoAlmacen = models.AutoField(primary_key=True)
    UsuarioAlta = models.CharField(max_length=10)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.CharField(max_length=10,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        ordering = ('-IdAlmacen',)
        db_table = "Almacenes"
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'

    def __str__(self):
        return f'{self.NombreAlmacen} ({self.IdAlmacen})'



class MarcasArticulos(models.Model):
    IdCategoria = models.CharField(max_length=8,db_index=True)
    IdMarca = models.IntegerField(db_index=True)
    DescripcionMarca = models.CharField(max_length=50)
    UsuarioAlta = models.CharField(max_length=10)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.CharField(max_length=10,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "MarcasArticulos"
        ordering = ('-IdMarca',)
        verbose_name = "MarcaArticulos"
        verbose_name_plural = "MarcasArticulos"
        index_together = (('IdCategoria','IdMarca'),)
        unique_together = (('IdCategoria','IdMarca'),)

    def __str__(self):
        return f'{self.DescripcionMarca} ({self.IdMarca})'


class PresentacionesArticulos(models.Model):
    IdCategoria = models.CharField(max_length=8,db_index=True)
    IdPresentacion = models.IntegerField(db_index=True)
    DescripcionPresentacion = models.CharField(max_length=50)
    UsuarioAlta = models.CharField(max_length=10)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.CharField(max_length=10,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "PresentacionesArticulos"
        ordering = ('-IdPresentacion',)
        verbose_name = 'PresentacionArticulos'
        verbose_name_plural = 'PresentacionesArticulos'
        index_together = (('IdCategoria','IdPresentacion'),)
        unique_together = (('IdCategoria','IdPresentacion'),)

    def __str__(self):
        return f'{self.DescripcionPresentacion} ({self.IdPresentacion})'


class ProductosSAT(models.Model):
    IdProductoSAT = models.IntegerField(primary_key=True,null=False,blank=False)
    DescripcionProductoSAT = models.CharField(max_length=256)
    IncluirIVATrasladoProductoSAT = models.CharField(max_length=1)
    IncluirIEPSRTrasladoProductoSAT = models.CharField(max_length=1)
    ComplementoProductoSAT = models.IntegerField(null=True)
    IncluidComplementoProductoSAT = models.CharField(max_length=1)
    CondicionMaterialPeligrosoProductoSAT = models.CharField(max_length=1)
    ClaveMaterialPeligrosoProductoSAT = models.CharField(max_length=5,null=True)
    ValorSistema = models.CharField(max_length=1)
    UsuarioAlta = models.CharField(max_length=10)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.CharField(max_length=10,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "ProductosSAT"
        ordering = ('-IdProductoSAT',)
        verbose_name = 'ProductoSAT'
        verbose_name_plural = 'ProductosSAT',

    def __str__(self):
        return f'{self.DescripcionProductoSAT} ({self.IdProductoSAT})'

class UnidadesSAT(models.Model):
    IdUnidadSAT = models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    NombreUnidadSAT = models.CharField(max_length=128)
    DescripcionUnidadSAT = models.CharField(max_length=640)
    NotaUnidadSAT = models.CharField(max_length=256)
    SimboloUnidadSAT = models.CharField(max_length=30)
    ValorSistema = models.CharField(max_length=1)
    UsuarioAlta = models.CharField(max_length=10)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.CharField(max_length=10,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "UnidadesSAT"
        ordering = ('-IdUnidadSAT',)
        verbose_name = 'UnidadSAT'
        verbose_name_plural = 'UnidadesSAT'

    def __str__(self):
        return f'{self.NombreUnidadSAT} ({self.IdUnidadSAT})'


class CategoriasArticulos(models.Model):
    IdCategoria = models.CharField(max_length=8,db_index=True,null=False,blank=False,unique=True)
    IdElementoCategoria = models.AutoField(primary_key=10)
    DescripcionCategoria = models.CharField(max_length=50)
    SubCategoria = models.CharField(max_length=8,null=True)
    CondicionExistenciaCategoria = models.CharField(max_length=1)
    SlugCategoria = models.SlugField(max_length=200,unique=True,blank=True)
    UsuarioAlta = models.CharField(max_length=10)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.CharField(max_length=10,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "CategoriasArticulos"
        ordering = ('-IdCategoria',)
        verbose_name = 'CategoriaArticulos'
        verbose_name_plural = 'CategoriasArticulos'
        unique_together = (('IdCategoria','SlugCategoria'))

    def save(self,*args,**kwargs):
        if not self.SlugCategoria:
            self.SlugCategoria = slugify(self.DescripcionCategoria)
        super(CategoriasArticulos,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.NombreCategoria} ({self.IdCategoria})';

    def get_absolute_url(self):
        return reverse("store:list_products_by_category",args=[self.SlugCategoria])

class Articulos(models.Model):
    IdCategoria = models.ForeignKey(CategoriasArticulos,related_name="categoriasArticulos",on_delete=models.PROTECT,db_index=True,db_column="IdCategoria",max_length=8)
    IdArticulo = models.IntegerField(db_index=True)
    NombreArticulo = models.CharField(max_length=256)
    EtiquetaArticulo = models.CharField(max_length=15)
    UPCArticulo = models.CharField(max_length=13,null=True)
    IdProductoSATArticulo = models.ForeignKey(ProductosSAT,related_name="productosSAT",on_delete=models.PROTECT,max_length=8,db_column="IdProductoSATArticulo")
    DescripcionArticulo = models.CharField(max_length=128)
    MarcaArticulo = models.ForeignKey(MarcasArticulos,related_name="marcas",on_delete=models.PROTECT,max_length=3,null=True,db_column="MarcaArticulo")
    ModeloArticulo = models.CharField(max_length=40)
    MedidaArticulo = models.CharField(max_length=5)
    UnidadMedidaArticulo = models.IntegerField(null=True)
    PresentacionArticulo = models.ForeignKey(PresentacionesArticulos,related_name="presentaciones",on_delete=models.PROTECT,max_length=3,null=True,db_column="PresentacionArticulo")
    FabricanteArticulo = models.IntegerField(null=True)
    ClaseArticulo = models.IntegerField()
    ProveedorPrimarioArticulo = models.IntegerField() #Pendiente tabla
    CotizacionesArticulo = models.IntegerField()
    ProcedenciaArticulo = models.CharField(max_length=1)
    ArancelArticulo = models.DecimalField(max_digits=7,decimal_places=2)
    MargenArticulo = models.DecimalField(max_digits=11,decimal_places=4)
    UnidadExistenciaArticulo = models.IntegerField()
    UnidadesEntradaArticulo = models.IntegerField()
    UnidadesSalidaArticulo = models.IntegerField()
    IdUnidadSATArticulo = models.ForeignKey(UnidadesSAT,related_name="unidadesSAT",on_delete=models.PROTECT,max_length=3,db_column="IdUnidadSATArticulo")
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
    FormatoImagenArticulo = models.CharField(max_length=50,null=True)
    NombreImagenArticulo = models.CharField(max_length=128,null=True)
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
    OperacionSATArticulo = models.IntegerField(null=True)
    IdElementoArticulo = models.AutoField(primary_key=True)
    SlugArticulo = models.SlugField(max_length=200,unique=True,blank=True)
    UsuarioAlta = models.CharField(max_length=10)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.CharField(max_length=10,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "Articulos"
        ordering = (('-IdCategoria'),)
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        unique_together = (('IdCategoria','IdArticulo'),)
        index_together = (('IdCategoria','IdArticulo'),)

    def save(self,*args,**kwargs):
        if not self.SlugArticulo:
            self.SlugArticulo = slugify(self.DescripcionArticulo)
        super(Articulos,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.NombreArticulo} ({self.IdArticulo})'

    def get_absolute_url(self):
        return reverse("store:product_detail",args=[self.IdArticulo,self.SlugArticulo])

class MarcasCategorias(models.Model):
    IdCategoria = models.ForeignKey(CategoriasArticulos,on_delete=models.CASCADE)
    IdMarca = models.ForeignKey(MarcasArticulos,on_delete=models.CASCADE)

    class Meta:
        unique_together = (('IdCategoria','IdMarca'),)

class PresentacionesCategorias(models.Model):
    IdCategoria = models.ForeignKey(CategoriasArticulos,on_delete=models.CASCADE)
    IdPresentacion = models.ForeignKey(PresentacionesArticulos,on_delete=models.CASCADE)

    class Meta:
        unique_together = (('IdCategoria','IdPresentacion'),)

class AlmacenArticulos(models.Model):
    IdAlmacen = models.ForeignKey(Almacenes,related_name="almacenesArticulos",on_delete=models.PROTECT,db_index=True,max_length=10,db_column="IdAlmacen")
    IdCategoria = models.ForeignKey(CategoriasArticulos,related_name="categoriasAlmacenArticulos",on_delete=models.PROTECT,db_index=True,max_length=8,db_column="IdCategoria")
    IdArticulo = models.ForeignKey(Articulos,related_name="articulosAlmacenArticulos",on_delete=models.PROTECT,db_index=True,max_length=10,db_column="IdArticulo")
    MaximoArticuloAlmacen = models.DecimalField(max_digits=14,decimal_places=3) #Nivel de inventario maximo (Cumplir pedidos y no sobrealmacenar)
    MinimoArtiuloAlmacen = models.DecimalField(max_digits=14,decimal_places=3) #Nivel de inventario minimo (Cantidad minima que se requiere para cubrir pedidos)
    ReordenArticuloAlmacen = models.DecimalField(max_digits=14,decimal_places=3)
    UbicacionArticuloAlmacen = models.CharField(max_length=6)
    ProveedorPrimarioArticuloAlmacen = models.IntegerField(null=True)
    IdElementoProveedor = models.AutoField(primary_key=True)
    UsuarioAlta = models.CharField(max_length=10)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.CharField(max_length=10,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "AlmacenArticulos"
        ordering = ('-IdAlmacen',)
        verbose_name = 'AlmacenArticulo'
        verbose_name_plural = 'AlmacenArticulos'
        index_together = (('IdAlmacen','IdCategoria','IdArticulo'),)
        unique_together = (('IdAlmacen','IdCategoria','IdArticulo'),)

class AlmacenArticuloExistencias(models.Model):
    IdAlmacen = models.ForeignKey(Almacenes,related_name="almacenesArticuloExistencias",on_delete=models.PROTECT,db_index=True,max_length=10,db_column="IdAlmacen")
    IdCategoria = models.ForeignKey(CategoriasArticulos,related_name="categoriasAlmacenArticuloExistencias",on_delete=models.PROTECT,db_index=True,max_length=8,db_column="IdCategoria")
    IdArticulo = models.ForeignKey(Articulos,related_name="articulosAlmacenArticuloExistencias",on_delete=models.PROTECT,db_index=True,max_length=10,db_column="IdArticulo")
    IdEstadoExistencia = models.IntegerField(db_index=True)
    EjercicioExistenciasArticulo = models.IntegerField(db_index=True)
    InicialExistenciasArticulo = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo01 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo02 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo03 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo04 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo05 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo06 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo07 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo08 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo09 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo10 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo11 = models.DecimalField(max_digits=16,decimal_places=3)
    EntradasExistenciasArticulo12 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo01 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo02 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo03 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo04 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo05 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo06 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo07 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo08 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo09 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo10 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo11 = models.DecimalField(max_digits=16,decimal_places=3)
    SalidasExistenciasArticulo12 = models.DecimalField(max_digits=16,decimal_places=3)
    IdElementoAlmacenArticuloExistencia = models.AutoField(primary_key=True)
    UsuarioAlta = models.CharField(max_length=10)
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.CharField(max_length=10,null=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField()
    Version = models.IntegerField()

    class Meta:
        db_table = "AlmacenArticuloExistencias"
        ordering = ['IdAlmacen','IdCategoria','IdArticulo']
        verbose_name = 'AlmacenArticuloExistencia'
        verbose_name_plural = 'AlmacenArticuloExistencias'
        index_together = (('IdAlmacen','IdCategoria','IdArticulo','IdEstadoExistencia','EjercicioExistenciasArticulo'),)
        unique_together = (('IdAlmacen','IdCategoria','IdArticulo','IdEstadoExistencia','EjercicioExistenciasArticulo'),)
