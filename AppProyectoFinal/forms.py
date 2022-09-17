from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppProyectoFinal.models import Amigo

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



class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(label="Ingrese Nombre")
    last_name= forms.CharField(label="Ingrese Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2' ]
        help_texts = {k:"" for k in fields}