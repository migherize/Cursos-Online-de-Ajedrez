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

class Contactanos(forms.Form):
    correo = forms.CharField(label='Correo', widget=forms.EmailInput(), max_length=100)
    mensaje = forms.CharField(max_length=300)