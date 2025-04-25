from django.db import models

# Create your models here.
class Empleados(models.Model):
    IdEmpleado = models.IntegerField(db_index=True)
    IdUsuario = models.OneToOneField('Usuarios',on_delete=models.CASCADE,db_column="IdUsuario",db_index=True,default=None)
    NombreEmpleado = models.CharField(max_length=30)
    ApellidoPaternoEmpleado = models.CharField(max_length=30)
    ApellidoMaternoEmpleado = models.CharField(max_length=30)
    DepartamentoEmpleado = models.CharField(max_length=50,null=True,blank=True)
    PuestoEmpleado = models.CharField(max_length=50,null=True,blank=True)
    FechaIngresoEmpleado = models.DateField(null=True,blank=True)
    FechaSalidaEmpleado = models.DateField(null=True,blank=True)
    RFCEmpleado = models.CharField(max_length=13,null=True,blank=True)
    SueldoBaseEmpleado = models.DecimalField(max_digits=22,decimal_places=6)
    ComisionVentaEmpleado = models.DecimalField(max_digits=7,decimal_places=2) # Porcentaje comision sobre ventas netas
    ComisionCobranzaEmpleado = models.DecimalField(max_digits=7,decimal_places=2) #Porcentaje comision sobre cobranza neta
    ImagenEmpleado = models.ImageField(upload_to='empleados/%Y/%m/%d', null=True,blank=True)
    FormatoImagenEmpleado = models.CharField(max_length=50,null=True,blank=True)
    NombreImagenEmpleado = models.CharField(max_length=128,null=True,blank=True)
    IdElementoEmpleado = models.AutoField(primary_key=True)
    UsuarioAlta = models.ForeignKey('Usuarios',to_field = 'IdUsuario',related_name='usuarioAltaEmpleados',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey('Usuarios',to_field = 'IdUsuario',related_name='usuarioCambioEmpleados',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True,blank=True)
    HoraCambio = models.TimeField(auto_now=True,null=True,blank=True)
    EstadoLogico = models.IntegerField(default=1)
    Version = models.IntegerField(default=0)

    class Meta:
        ordering = ('-IdEmpleado',)
        db_table = "empleados"
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        index_together = (('IdEmpleado','IdUsuario'),)
        unique_together = (('IdEmpleado','IdUsuario'),)

    def __str__(self):
        return f'{self.NombreEmpleado} {self.ApellidoPaternoEmpleado} ({self.IdEmpleado})'

class Usuarios(models.Model):
    IdUsuario = models.CharField(db_index=True,max_length=10,unique=True)
    CredencialUsuario = models.CharField(max_length=256,null=True,blank=True)
    NombreUsuario = models.CharField(max_length=30)
    ApellidoPaternoUsuario = models.CharField(max_length=30)
    ApellidoMaternoUsuario = models.CharField(max_length=30)
    CuentaCorreoUsuario = models.CharField(max_length=100)
    GrupoUsuario = models.CharField(max_length=30)
    ImagenUsuario = models.ImageField(upload_to='usuarios/%Y/%m/%d', null=True,blank=True)
    FormatoImagenUsuario = models.CharField(max_length=50,null=True,blank=True)
    NombreImagenUsuario = models.CharField(max_length=128,null=True,blank=True)
    LimiteConsumosUsuario = models.DecimalField(max_digits=24,decimal_places=6) #Importe maximo que el usuario esta autorizado a consumir
    LimiteAutorizaConsumosUsuario = models.DecimalField(max_digits=24,decimal_places=6) #Importe maximo autorizado para una requisicion de almacen
    LimiteComprasUsuario = models.DecimalField(max_digits=24,decimal_places=6) #Importe maximo que esta autorizado a comprar
    LimiteAutorizaComprasUsuario = models.DecimalField(max_digits=24,decimal_places=6) #Importe maximo que el usuario puede autorizar en una compra
    LimiteAutorizaPagosUsuario = models.DecimalField(max_digits=24,decimal_places=6) #Importe maximo que el usuario puede autorizar en un pago
    LimiteAutorizaVentaUsuario = models.DecimalField(max_digits=24,decimal_places=6) #Importe maximo que el usuario puede autorizar en una venta a credito
    PorcentajeMaximoVentaUsuario = models.DecimalField(max_digits=7,decimal_places=2) #Porcetaje maximo de descuento que puede autorizar un usuario
    NivelAutorizacionUsuario = models.CharField(max_length=1)
    IdElementoUsuario = models.AutoField(primary_key=True)
    UsuarioAlta = models.ForeignKey('self',to_field = 'IdUsuario',related_name='usuarioAltaUsuarios',on_delete=models.PROTECT,db_column="UsuarioAlta")
    FechaAlta = models.DateField(auto_now_add=True)
    HoraAlta = models.TimeField(auto_now_add=True)
    UsuarioCambio = models.ForeignKey('self',to_field = 'IdUsuario',related_name='usuarioCambioUsuarios',on_delete=models.PROTECT,db_column="UsuarioCambio",null=True,blank=True)
    FechaCambio = models.DateField(auto_now=True,null=True,blank=True)
    HoraCambio = models.TimeField(auto_now=True,null=True,blank=True)
    EstadoLogico = models.IntegerField(default = 1)
    Version = models.IntegerField(default = 0)

    class Meta:
        ordering = ('-IdUsuario',)
        db_table = "usuarios"
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.NombreUsuario} {self.ApellidoPaternoUsuario} ({self.IdUsuario})'
