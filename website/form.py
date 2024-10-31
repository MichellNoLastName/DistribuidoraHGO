from django import forms
from allauth.account.forms import SignupForm
from .models import Usuarios
from orders.models import ContactoMedios,Catalogos

class CustomSignupForm(SignupForm):
    # Agrega los campos adicionales
    email = forms.EmailField(max_length=50,required=True,label='Correo Electrónico',
        error_messages={
            'required': 'Por favor, ingresa tu dirección de correo electrónico.',
            'invalid': 'Ingresa una dirección de correo electrónico válida.',
        })
    first_name = forms.CharField(max_length=30, required=True, label='Nombres(s)',widget=forms.TextInput(attrs={
            'pattern': r'[A-Za-z]+',  # Solo permite letras
            'title': 'Por favor, ingresa solo letras.'
        }),error_messages={
            'required': 'Este campo es obligatorio.',
            'max_length': 'El nombre no puede exceder 30 caracteres.',
        })
    last_name = forms.CharField(max_length=30, required=True, label='Apellido Paterno',widget=forms.TextInput(attrs={
            'pattern': r'[A-Za-z]+',  # Solo permite letras
            'title': 'Por favor, ingresa solo letras.'
        }),error_messages={
            'required': 'Este campo es obligatorio.',
            'max_length': 'El apellido paterno no puede exceder 30 caracteres.',
        })
    apellidoMaternoUsuario = forms.CharField(max_length=30, required=False, label='Apellido Materno',widget=forms.TextInput(attrs={
            'pattern': r'[A-Za-z]+',  # Solo permite letras
            'title': 'Por favor, ingresa solo letras.'
        }),error_messages={
            'required': 'Este campo es obligatorio.',
            'max_length': 'El apellido paterno no puede exceder 30 caracteres.',
        }
        )
    numeroTelefonicoUsuario = forms.CharField(label="Número Telefónico",max_length=10,min_length=10,error_messages={'max_length': 'El número debe tener 10 dígitos.', 'min_length': 'El número debe tener 10 dígitos.'},
                                                   widget=forms.TextInput(attrs={'type': 'tel', 'pattern': '\d{10}', 'title': 'Debe contener exactamente 10 dígitos'}))



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Elimina el campo de username del formulario
        self.fields.pop('username')
        self.fields['numeroTelefonicoUsuario'].widget.attrs['placeholder'] = 'Ej. 1122223344'

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        username = (self.cleaned_data['first_name'][0].upper() +
                     self.cleaned_data['last_name'].upper())

        user2 = Usuarios(IdUsuario=username,
                         NombreUsuario=self.cleaned_data['first_name'].strip(),
                         ApellidoPaternoUsuario=self.cleaned_data['last_name'].strip(),
                         ApellidoMaternoUsuario=self.cleaned_data['apellidoMaternoUsuario'].strip(),
                         CuentaCorreoUsuario=self.cleaned_data['email'],
                         GrupoUsuario='Clientes',
                         ImagenUsuario=None,
                         FormatoImagenUsuario=None,
                         NombreImagenUsuario=None,
                         LimiteConsumosUsuario=1000000,
                         LimiteAutorizaConsumosUsuario=0.0,
                         LimiteComprasUsuario=1000000,
                         LimiteAutorizaComprasUsuario=0.0,
                         LimiteAutorizaPagosUsuario=0.0,
                         LimiteAutorizaVentaUsuario=0.0,
                         PorcentajeMaximoVentaUsuario=100,
                         NivelAutorizacionUsuario='C',
                         EstadoLogico=1,
                         Version=0
                         )

        #Creacion de datos de contacto
        tipoMedioContactoTelefono = Catalogos.objects.get(IdCatalogo=6,ElementoCatalogo=169)
        tipoMedioContactoEmail = Catalogos.objects.get(IdCatalogo=6,ElementoCatalogo=178)

        telefonoMedioContacto = ContactoMedios(
            TipoMedioContacto = tipoMedioContactoTelefono,
            UsuarioContactoMedio = user2,
            DatoTipoMedioContacto = self.cleaned_data['numeroTelefonicoUsuario'],
            PrimarioMedioContacto = 'S',
            EstadoLogico=1,
            Version=0,
        )

        correoMedioContacto = ContactoMedios(
            TipoMedioContacto = tipoMedioContactoEmail,
            UsuarioContactoMedio = user2,
            DatoTipoMedioContacto = self.cleaned_data['email'],
            PrimarioMedioContacto = 'N',
            EstadoLogico=1,
            Version=0,
        )

        user2.save(request)
        telefonoMedioContacto.save(request)
        correoMedioContacto.save(request)

        return user
