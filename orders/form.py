import random
from django import forms
from django.db import connection
from .models import OrdenesCliente,EntidadesFederativas,Localidades,Colonias,Usuarios,ContactoMedios

class AddOrderForm(forms.ModelForm):
    IdOrdenCliente = forms.IntegerField(label="Orden")
    NombreOrdenCliente = forms.CharField(label="Nombre Completo",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    ApellidoPaternoOrdenCliente = forms.CharField(label="Apellido Paterno",widget=forms.TextInput(attrs={'class':'form-control'}))
    ApellidoMaternoOrdenCliente = forms.CharField(label="Apellido Materno",widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    CorreoElectronicoOrdenCliente = forms.EmailField(label="Correo Electrónico",widget=forms.EmailInput(attrs={'class':'form-control'}))
    NumeroTelefonicoOrdenCliente = forms.CharField(label="Número Telefónico",max_length=10,min_length=10,error_messages={'max_length': 'El número debe tener 10 dígitos.', 'min_length': 'El número debe tener 10 dígitos.'},
                                                   widget=forms.TextInput(attrs={'type': 'tel', 'pattern': '\d{10}', 'title': 'Debe contener exactamente 10 dígitos'})
    )
    CodigoPostalOrdenCliente = forms.IntegerField(label="Código Postal (Escribe tu código postal y presiona Enter para validarlo)",widget=forms.NumberInput(attrs={'class':'form-control','type': 'tel', 'pattern': '\d{5}', 'title': 'El Código Postal no es correcto'}))
    EntidadFederativaOrdenCliente = forms.ModelChoiceField(queryset=EntidadesFederativas.objects.all().order_by('NombreEntidadFederativa'))
    LocalidadOrdenCliente = forms.ModelChoiceField(queryset=Localidades.objects.none())
    ColoniaOrdenCliente = forms.ModelChoiceField(queryset=Colonias.objects.none())
    DomicilioOrdenCliente = forms.CharField(label="Domicilio",widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = OrdenesCliente
        fields = ['IdOrdenCliente','NombreOrdenCliente','ApellidoPaternoOrdenCliente','ApellidoMaternoOrdenCliente',
                  'CorreoElectronicoOrdenCliente','NumeroTelefonicoOrdenCliente','CodigoPostalOrdenCliente',
                  'EntidadFederativaOrdenCliente','LocalidadOrdenCliente','ColoniaOrdenCliente','DomicilioOrdenCliente']

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

        self.fields['IdOrdenCliente'].widget.attrs['disabled'] = True

        result = "NOK"
        while result != "OK":
            ordenId = random.randint(10**6,10**7)
            with connection.cursor() as cursor:
                cursor.execute("SELECT fn_ValidarIdOrdenCuenta(%s)",params=[ordenId])
                result = cursor.fetchone()[0]


        self.fields['IdOrdenCliente'].initial = ordenId

        if 'idEntidadFederativa' in self.data:
            try:
                idEntidadFederativa = int(self.data.get('idEntidadFederativa'))
                self.fields['LocalidadOrdenCliente'].queryset = Localidades.objects.filter(IdEntidadFederativa = idEntidadFederativa).order_by('NombreLocalidad')
            except(ValueError,TypeError):
                pass

    def save(self,request):
        userCliente = Usuarios.objects.get(IdUsuario = request.user)
        emailCliente = ContactoMedios.objects.get(UsuarioContactoMedio = userCliente,TipoMedioContacto=178)
        numeroTelefonicoCliente = ContactoMedios.objects.get(UsuarioContactoMedio = userCliente, TipoMedioContacto = 169)

        self.cleaned_data['CorreoElectronicoOrdenCliente'] = emailCliente
        self.cleaned_data['NumeroTelefonicoOrdenCliente'] = numeroTelefonicoCliente

        super(AddOrderForm,self).save(request)
