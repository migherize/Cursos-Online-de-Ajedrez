from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.ChessLive,name='chess-live'),
	path('login/', views.signUp, name='login'),
	path('register/', views.register, name='register'),
	path('forget/', views.forget, name='forget'),
	path('main/', views.main, name='main'),

]