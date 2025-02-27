from django import forms
from .models import Adrress

class CepForm(forms.ModelForm):




class AdrressForm(forms.ModelForm):
    class Meta:
        model = Adrress
        fields =['cep', 'logradouro', 'bairro', 'localidade', 'uf']
        labels = {
            'cep': 'CEP',
            'logradouro': 'Logradouro',
            'bairro': 'Bairro',
            'localidade': 'Localidade',
            'uf': 'UF'
        }
        widgets = {
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'localidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'})
        }