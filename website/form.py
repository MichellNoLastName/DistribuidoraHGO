from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    # Agrega los campos adicionales
    nombreCompletoUsuario = forms.CharField(max_length=30, required=True, label='Nombres(s)')
    apellidoPaternoUsuario = forms.CharField(max_length=30, required=True, label='Apellido Paterno')
    apellidoMaternoUsuario = forms.CharField(max_length=30, required=False, label='Apellido Materno')
    numeroTelefonicoUsuario = forms.IntegerField(required=True,label="Número Telefonico")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Elimina el campo de username del formulario
        self.fields.pop('username')
        self.fields['numeroTelefonicoUsuario'].widget.attrs['placeholder'] = 'Ej. 7712223344'

    def save(self, commit=True):
        user = super(CustomSignupForm, self).save(commit=False)
        if commit:
            user.save()
        return user
