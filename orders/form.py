from django import forms
from .models import OrdenesCliente

class AddOrderForm(forms.ModelForm):
    NombreOrdenCliente = forms.CharField(label="Nombre Completo",widget=forms.TextInput(attrs={'class':'form-control'}))
    ApellidoPaternoOrdenCliente = forms.CharField(label="Apellido Paterno",widget=forms.TextInput(attrs={'class':'form-control'}))
    ApellidoMaternoOrdenCliente = forms.CharField(label="Apellido Materno",widget=forms.TextInput(attrs={'class':'form-control'}))
    CorreoElectronicoOrdenCliente = forms.EmailField(label="Correo Electrónico",widget=forms.EmailInput(attrs={'class':'form-control'}))
    NumeroTelefonicoOrdenCliente = forms.CharField(label="Teléfono",max_length=10,widget=forms.NumberInput(attrs={'class':'form-control'}))
    CodigoPostalOrdenCliente = forms.CharField(label="Código Postal",max_length=6,widget=forms.NumberInput(attrs={'class':'form-control'}))
    DomicilioOrdenCliente = forms.CharField(label="Domicilio",widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = OrdenesCliente
        fields = ['NombreOrdenCliente','ApellidoPaternoOrdenCliente','ApellidoMaternoOrdenCliente',
                  'CorreoElectronicoOrdenCliente','NumeroTelefonicoOrdenCliente','CodigoPostalOrdenCliente',
                  'EntidadFederativaOrdenCliente','LocalidadOrdenCliente','ColoniaOrdenCliente','DomicilioOrdenCliente']

    def __init__(self,*args,**kwargs):
        super(AddOrderForm, self).__init__(*args,**kwargs)

        self.fields['EntidadFederativaOrdenCliente'].label = 'Entidad Federativa'
        self.fields['LocalidadOrdenCliente'].label = 'Localidad'
        self.fields['ColoniaOrdenCliente'].label = 'Colonia'
