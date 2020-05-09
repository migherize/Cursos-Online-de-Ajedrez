from django import forms
from django.contrib.auth.models import User
from .models import  *
from django.contrib.auth.forms import UserCreationForm

class Login(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), max_length=100)

class Register(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.CharField(label='Correo', widget=forms.EmailInput(), max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), max_length=100)
    tipo = forms.CharField(label='tipo', max_length=1)

class Contactanos(forms.Form):
    correo = forms.CharField(label='Correo', widget=forms.EmailInput(), max_length=100)
    mensaje = forms.CharField(max_length=300)

class Perfile (forms.Form):
	first_name = forms.CharField(label='Nombre', max_length=30)
	last_name = forms.CharField(label='Apellido', max_length=30)
	sexo = forms.CharField(label='Sexo', max_length=1)
	pais = forms.CharField(label='Pais', max_length=30)
	titulo = forms.CharField(label='Titulo', max_length=30)
	ruta = forms.CharField(label='Foto', max_length=30)
	Fide = forms.CharField(label='ID Fide', max_length=30)


class Prueba(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    tipos= [('P','Profesor'),('A','Alumno')]
    tipo = forms.CharField(label='Tipo',widget=forms.RadioSelect(choices=tipos))
