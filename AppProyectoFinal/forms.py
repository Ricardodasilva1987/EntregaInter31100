from django import forms
from django.contrib.auth.forms import UserCreationForm

class AmigosFormulario(forms.Form):
    nombre =forms.CharField(max_length=30)
    raza = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    duenio= forms.CharField(max_length=50)



class JuguetesFormulario(forms.Form):
    nombre =forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=50)


class LugaresFormulario(forms.Form):    
    nombre =forms.CharField(max_length=30)
    horario = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=100)


class ComidaFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    calorias = forms.IntegerField()
    recomendable = forms.BooleanField()

#class UserRegisterForm(UserCreationForm):

