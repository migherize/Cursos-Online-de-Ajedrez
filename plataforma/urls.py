from django.urls import path
from . import views

urlpatterns = [
	path('',views.ChessLive,name='chess-live'),
	path('login/', views.signUp, name='login'),
	path('register/', views.register, name='register'),
	path('forget/', views.forget, name='forget'),
	path('logout/', views.signOut, name='logout'),
	path('main/', views.main, name='main'),
	path('contactanos/', views.contact, name='contact'),
	path('perfil/', views.perfil, name='perfil'),

]