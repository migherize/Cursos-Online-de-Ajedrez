from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from django.core.mail import EmailMessage
# Create your views here.

def ChessLive(request):
	return render(request, 'plataforma/chess-live.html', {})

def signUp(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Login(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	username = form.cleaned_data['username']
        	password = form.cleaned_data['password']
        	print(username,password)
        	user = authenticate(username=username, password=password)
        	print("user2",user)
        	if user is not None:
        		login(request, user)
        		print("Bienvenido")
        		return render(request, 'plataforma/main.html', {})
        	else:
        		print("No estas logiado, registrate")
        		return HttpResponseRedirect('/Login/')
    else:
    	form = Login()

    print("debe escribir")
    return render(request, 'plataforma/login.html', {'form': form})

def register(request):
	if request.method == 'POST':
		form = Register(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = User.objects.create_user(username, email, password)
			return HttpResponseRedirect('/login/')
	else:
		print("Debe llenar todo")
		form = Register

	return	render(request, 'plataforma/register.html', {})

def forget(request):
	return render(request, 'plataforma/forget.html',{})

def signOut(request):
	logout(request)
	print("Hasta Luego")
	return HttpResponseRedirect('/login/')

def contact(request):
    if request.method == 'POST':
        formulario = Contactanos(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde chess-live de'
            for i in formulario:
                print("i",i)
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido = contenido + formulario.cleaned_data['correo']
            print(titulo,contenido)
            correo = EmailMessage(titulo, contenido,to = ['manherize@gmail.com'])
            correo.send()
            print("envio")
            return HttpResponseRedirect('/')
    else:
        formulario = Contactanos
    return render(request, 'plataforma/contact.html',{'formulario': formulario})

def main(request):
	return render(request, 'plataforma/main.html',{})

def perfil(request):
	return render(request, 'plataforma/perfil.html',{})