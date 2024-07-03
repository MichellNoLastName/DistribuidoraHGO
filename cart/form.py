from django import forms

OPTION_PRODUCTS = [(i,str(i)) for i in range(1,21)]

class AddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=OPTION_PRODUCTS,
                                      coerce=int,label="Cantidad")
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
