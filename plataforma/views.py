from django.shortcuts import render

# Create your views here.

def ChessLive(request):
	return render(request, 'plataforma/chess-live.html', {})

def signUp(request):
	return	render(request, 'plataforma/login.html', {})

def register(request):
	return	render(request, 'plataforma/register.html', {})

def forget(request):
	return render(request, 'plataforma/forget.html',{})

def main(request):
	return render(request, 'plataforma/main.html',{})