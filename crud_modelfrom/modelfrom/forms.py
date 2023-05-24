from django.core import validators
from django import forms
from .models import Vser


class Registion (forms.ModelForm):
    class Meta:
        model = Vser
        fields = ("name", "email", "password", "massages")
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput( render_value=True, attrs={'class':'form-control'}),
            'massages': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':40}),
         }