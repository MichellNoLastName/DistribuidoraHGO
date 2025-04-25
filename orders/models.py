from django.db import models
from django.db.models import UniqueConstraint
from website.models import Usuarios
from store.models import Articulos,Catalogos

# Create your models here.
class EntidadesFederativas(models.Model):
    IdEntidadFederativa = models.AutoField(primary_key=True,db_index=True,unique=True)
    NombreEntidadFederativa = models.CharField(max_length=30)
    EtiquetaEntidadFederativa = models.CharField(max_length=5)
    HusoHorarioEntidadFederativa = models.IntegerField()
    ValorSistema = models.CharField(max_length=1)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaEntidadesFederativas',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioEntidadesFederativas',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'entidadesfederativas'
        verbose_name = 'EntidadFederativa'
        verbose_name_plural = 'EntidadesFederativas'
        ordering = ('-IdEntidadFederativa',)

    def __str__(self):
        return f'{self.NombreEntidadFederativa}'

class Localidades(models.Model):
    IdEntidadFederativa = models.ForeignKey(EntidadesFederativas,related_name='entidadesFederativasLocalidades',to_field='IdEntidadFederativa',on_delete=models.PROTECT,db_column='IdEntidadFederativa',db_index=True)
    IdLocalidad = models.IntegerField(db_index=True)
    NombreLocalidad = models.CharField(max_length=50)
    ValorSistema = models.CharField(max_length=1)
    IdElementoLocalidad = models.AutoField(primary_key=True,default=None)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaLocalidades',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioLocalidades',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'localidades'
        ordering = ('-IdLocalidad',)
        verbose_name='Localidad'
        verbose_name_plural = 'Localidades'
        index_together = (('IdEntidadFederativa','IdLocalidad'),)
        unique_together = (('IdEntidadFederativa','IdLocalidad'),)

    def __str__(self):
        return f'{self.NombreLocalidad}'

class CodigosPostales(models.Model):
    IdEntidadFederativa = models.ForeignKey(EntidadesFederativas,related_name='entidadesFederativasCP',to_field='IdEntidadFederativa',on_delete=models.PROTECT,db_column='IdEntidadFederativa',db_index=True)
    IdLocalidad = models.ForeignKey(Localidades,related_name='localidadesCP',to_field='IdElementoLocalidad',on_delete=models.PROTECT,db_column='IdLocalidad',db_index=True)
    IdCodigoPostal = models.IntegerField(db_index=True,unique=True)
    IdElementoCodigoPostal = models.AutoField(primary_key=True,default=None)
    ValorSistema = models.CharField(max_length=1)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaCP',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioCP',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'codigospostales'
        ordering = ('-IdCodigoPostal',)
        verbose_name = 'CodigoPostal'
        verbose_name_plural = 'CodigosPostales'
        unique_together = (('IdEntidadFederativa','IdLocalidad','IdCodigoPostal'),)
        index_together = (('IdEntidadFederativa','IdLocalidad','IdCodigoPostal'),)

    def __str__(self):
        return f'{self.IdCodigoPostal}'

class Colonias(models.Model):
    IdEntidadFederativa = models.ForeignKey(EntidadesFederativas,related_name='entidadesFederativasColonias',to_field='IdEntidadFederativa',on_delete=models.PROTECT,db_column='IdEntidadFederativa',db_index=True)
    IdLocalidad = models.ForeignKey(Localidades,related_name='localidadesColonias',to_field='IdElementoLocalidad',on_delete=models.PROTECT,db_column='IdLocalidad',db_index=True)
    IdCodigoPostal = models.ForeignKey(CodigosPostales,related_name='cpColonias',to_field='IdCodigoPostal',on_delete=models.PROTECT,db_column='IdCodigoPostal',db_index=True)
    IdColonia = models.IntegerField(db_index=True)
    NombreColonia = models.CharField(max_length=60)
    ValorSistema = models.CharField(max_length=1)
    IdElementoColonia = models.AutoField(primary_key=True,default=None)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaColonias',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioColonias',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'colonias'
        ordering = ('-IdColonia',)
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'
        unique_together = (('IdEntidadFederativa','IdLocalidad','IdCodigoPostal','IdColonia'),)
        index_together = (('IdEntidadFederativa','IdLocalidad','IdCodigoPostal','IdColonia'),)

    def __str__(self):
        return f'{self.NombreColonia}'

class ContactoMedios(models.Model):
    IdContactoMedio = models.AutoField(primary_key=True)
    UsuarioContactoMedio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuariosContactoMedios',on_delete=models.PROTECT,db_column='UsuarioContactoMedio',db_index=True)
    TipoMedioContacto = models.ForeignKey(Catalogos,to_field='ElementoCatalogo',related_name='tiposMediosContactoMedios',on_delete=models.PROTECT,db_column='TipoMedioContacto',db_index=True)
    DatoTipoMedioContacto = models.CharField(max_length=64)
    PrimarioMedioContacto = models.CharField(max_length=1) #Si/ NO
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaContactoMedios',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioContactoMedios',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'contactomedios'
        verbose_name = 'ContactoMedio'
        verbose_name_plural = 'ContactoMedios'
        index_together = (('UsuarioContactoMedio','TipoMedioContacto'),)
        unique_together = (('UsuarioContactoMedio','TipoMedioContacto'),)

    def __str__(self):
        return f'{self.DatoTipoMedioContacto} ({self.UsuarioContactoMedio})'


class OrdenesCliente(models.Model):
    IdOrdenCliente = models.IntegerField(db_index=True,unique=True)
    UsuarioOrdenCliente = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuariosOrdenesCliente',on_delete=models.PROTECT,db_column='UsuarioOrdenCliente')
    NombreOrdenCliente = models.CharField(max_length=30)
    ApellidoPaternoOrdenCliente = models.CharField(max_length=30)
    ApellidoMaternoOrdenCliente = models.CharField(max_length=30,null=True,blank=True)
    CorreoElectronicoOrdenCliente = models.EmailField()
    NumeroTelefonicoOrdenCliente = models.CharField(max_length=10)
    CodigoPostalOrdenCliente = models.IntegerField()
    EntidadFederativaOrdenCliente = models.CharField(max_length=100)
    LocalidadOrdenCliente = models.CharField(max_length=200)
    ColoniaOrdenCliente = models.CharField(max_length=100)
    DomicilioOrdenCliente = models.CharField(max_length=1023)
    PagoOrdenCliente = models.BooleanField(default=False)
    IdElementoOrdenCliente = models.AutoField(primary_key=True,default=None)
    UsuarioAlta = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioAltaOrdenesCliente',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey(Usuarios,to_field='IdUsuario',related_name='usuarioCambioOrdenesCliente',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True)
    HoraCambio = models.TimeField(auto_now=True,null=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        db_table = 'ordenescliente'
        ordering = ('-FechaAlta','-HoraAlta','-IdOrdenCliente',)
        verbose_name = 'OrdenCliente',
        verbose_name_plural = 'OrdenesClientes'
        index_together = (('IdOrdenCliente','UsuarioOrdenCliente'),)
        unique_together = (('IdOrdenCliente','UsuarioOrdenCliente'),)

    def __str__(self):
        return f'Orden #{self.IdOrdenCliente}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class ItemOrdenesCliente(models.Model):
    IdItemOrden = models.AutoField(primary_key=True,db_index=True,unique=True)
    OrdenItemOrden = models.ForeignKey(OrdenesCliente,related_name='ordenesItemOrden',to_field='IdOrdenCliente',on_delete=models.CASCADE,db_column='OrdenItemOrden')
    ArticuloItemOrden = models.ForeignKey(Articulos,related_name='articulosItemOrden',to_field='IdArticulo',on_delete=models.PROTECT,db_column='ArticuloItemOrden')
    PrecioItemOrden = models.DecimalField(max_digits=22,decimal_places=6)
    CantidadItemOrden = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'itemordencliente'
        verbose_name = 'ItemOrdenCliente'
        verbose_name_plural = 'ItemOrdenesCliente'

    def __str__(self):
        return self.IdItemOrden

    def get_cost(self):
        return (self.PrecioItemOrden * self.CantidadItemOrden)
