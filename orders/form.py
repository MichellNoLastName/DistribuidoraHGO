from django import forms
from django.db import connection
from .models import OrdenesCliente,EntidadesFederativas,Localidades,Colonias,Usuarios

class AddOrderForm(forms.ModelForm):
    IdOrdenCliente = forms.IntegerField(label="Orden")
    UsuarioOrdenCliente = forms.ModelChoiceField(queryset=Usuarios.objects.all(), empty_label="Seleccione un usuario")
    NombreOrdenCliente = forms.CharField(label="Nombre Completo",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    ApellidoPaternoOrdenCliente = forms.CharField(label="Apellido Paterno",widget=forms.TextInput(attrs={'class':'form-control'}))
    ApellidoMaternoOrdenCliente = forms.CharField(label="Apellido Materno",widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    CorreoElectronicoOrdenCliente = forms.EmailField(label="Correo Electrónico",widget=forms.EmailInput(attrs={'class':'form-control'}))
    NumeroTelefonicoOrdenCliente = forms.CharField(label="Número Telefónico",max_length=10,min_length=10,error_messages={'max_length': 'El número debe tener 10 dígitos.', 'min_length': 'El número debe tener 10 dígitos.'},
                                                   widget=forms.TextInput(attrs={'type': 'tel', 'pattern': '\d{10}', 'title': 'Debe contener exactamente 10 dígitos'})
    )
    CodigoPostalOrdenCliente = forms.IntegerField(label="Código Postal (Escribe tu código postal y presiona Enter para validarlo)",widget=forms.NumberInput(attrs={'class':'form-control','type': 'tel', 'pattern': '\d{5}', 'title': 'El Código Postal no es correcto'}))
    EntidadFederativaOrdenCliente = forms.ModelChoiceField(queryset=EntidadesFederativas.objects.all().order_by('NombreEntidadFederativa'))
    LocalidadOrdenCliente = forms.ModelChoiceField(queryset=Localidades.objects.all())
    ColoniaOrdenCliente = forms.ModelChoiceField(queryset=Colonias.objects.all())
    DomicilioOrdenCliente = forms.CharField(label="Domicilio",widget=forms.Textarea(attrs={'class':'form-control'}))
    UsuarioAlta = forms.ModelChoiceField(queryset=Usuarios.objects.all(), empty_label="Seleccione un usuario")

    class Meta:
        model = OrdenesCliente
        fields = ['IdOrdenCliente','UsuarioOrdenCliente','NombreOrdenCliente','ApellidoPaternoOrdenCliente','ApellidoMaternoOrdenCliente',
                  'CorreoElectronicoOrdenCliente','NumeroTelefonicoOrdenCliente','CodigoPostalOrdenCliente',
                  'EntidadFederativaOrdenCliente','LocalidadOrdenCliente','ColoniaOrdenCliente','DomicilioOrdenCliente','UsuarioAlta']

    def __init__(self,*args,**kwargs):
        super(AddOrderForm, self).__init__(*args,**kwargs)

        self.fields['CodigoPostalOrdenCliente'].widget.attrs['title'] = 'Escribe tu codigo postal y presiona Enter para validarlo'
        self.fields['EntidadFederativaOrdenCliente'].label = 'Entidad Federativa'
        self.fields['EntidadFederativaOrdenCliente'].empty_label = '--- Seleccione una opción---'
        self.fields['LocalidadOrdenCliente'].label = 'Localidad'
        self.fields['LocalidadOrdenCliente'].empty_label = '--- Seleccione una opción---'
        self.fields['LocalidadOrdenCliente'].widget.attrs['disabled'] = 'disabled'
        self.fields['ColoniaOrdenCliente'].label = 'Colonia'
        self.fields['ColoniaOrdenCliente'].empty_label = '--- Seleccione una opción---'
        self.fields['ColoniaOrdenCliente'].widget.attrs['disabled'] = 'disabled'
        self.fields['DomicilioOrdenCliente'].widget.attrs['placeholder'] = "Num Exterior, Num Interior, Calle y detalles de domicilio"

        self.fields['IdOrdenCliente'].widget.attrs.update({'style': 'pointer-events: none;'})
        self.fields['UsuarioOrdenCliente'].label = ''
        self.fields['UsuarioOrdenCliente'].widget.attrs.update({'style': 'display: none;'})
        self.fields['UsuarioAlta'].label = ''
        self.fields['UsuarioAlta'].widget.attrs.update({'style': 'display: none;'})
