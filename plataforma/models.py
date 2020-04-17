from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Zona de Perfil
class Perfil(models.Model):
	genero = (
		('F','Femenino'),
		('M','Masculo'),
	)
	sexo = models.CharField(max_length=1, choices = genero)

	title = (
		('CM','Candidato Maestro'),
		('MF','Maestro Fide'),
		('MI','Maestro Internacional'),
		('GM','Gran Maestro'),
	)
	titulo = models.CharField(max_length=2, choices = title)
	
	user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

class Foto(models.Model):
	ruta = models.ImageField(
		upload_to ='../imagenes/Profiles/', height_field=None, width_field=None, max_length=100)
	
	perfil =models.OneToOneField(Perfil, null=True, blank=True, on_delete=models.CASCADE)

class Direccion(models.Model):
	calle = models.CharField(max_length=30, null=True, blank=True, default=None)
	avenida = models.CharField(max_length=30, null=True, blank=True, default=None)
	cuidad = models.CharField(max_length=30, null=True, blank=True, default=None)
	pais = models.CharField(max_length=30, null=True, blank=True, default=None)

	perfil = models.ForeignKey(Perfil, related_name="addresses", on_delete=models.CASCADE)

class ELO(models.Model):
	Type = models.CharField(max_length=10, primary_key=True)
	Num_win = models.IntegerField()
	Num_lose = models.IntegerField()
	Num_draw = models.IntegerField()

	perfil = models.ForeignKey(Perfil, related_name="rankings", null=True, blank=True, on_delete=models.CASCADE)



#Zona de clase 

class Curso(models.Model):
	nombre = models.CharField(max_length=30, null=True, blank=True, default=None)

class Estudiante(models.Model):
	promedio = models.IntegerField()
	user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

class Tutor(models.Model):
	Salario = models.IntegerField()
	User = models.OneToOneField('auth.User', on_delete=models.CASCADE)

class Seccion_De(models.Model):
	fecha_inicio =  models.DateTimeField()
	fecha_fin =  models.DateTimeField()
	costo = models.IntegerField()
	
	curso = models.ForeignKey(Curso, related_name="clase",null=True, blank=True, on_delete=models.CASCADE)

class Seccion(models.Model):
	nombre = models.CharField(max_length=30, null=True, blank=True, default=None)

	seccion_de = models.ForeignKey(Seccion_De,related_name ="modulo", null=True, blank=True, on_delete=models.CASCADE)
	tutor = models.ForeignKey(Tutor, related_name ="profesor", null=True, blank=True, on_delete=models.CASCADE)

class Asiste_a(models.Model):
	nota = models.IntegerField()

	seccion = models.ManyToManyField(Seccion)
	estudiante = models.ManyToManyField(Estudiante)

#Zona de Amigos

class Amigo(models.Model):
	
	aceptar = models.BooleanField(default=False)

	followers = models.ForeignKey('auth.User', null=True,related_name="seguidores", blank=True, on_delete=models.CASCADE)
	follow = models.ForeignKey('auth.User', null=True,related_name="seguidor", blank=True, on_delete=models.CASCADE)

	class Meta:
		unique_together = ['followers','follow']

#Zona de Partida

class Estructura_peones(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)
	
	estilo = models.ForeignKey('Estilo_de_Partida', related_name="estructura", null=True, blank=True, on_delete=models.CASCADE)

class Tipo(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)

class Apertura(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=30)

class Medio_Juego(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)

	estilo = models.ForeignKey('Estilo_de_Partida', related_name="mediojuego", null=True, blank=True, on_delete=models.CASCADE)

class Final(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)

	estilo = models.ForeignKey('Estilo_de_Partida', related_name="final", null=True, blank=True, on_delete=models.CASCADE)

class Partida(models.Model):
	user = models.CharField(max_length=30)
	contrincante = models.CharField(max_length=30)
	fecha_hora =  models.DateTimeField()
	resultado = models.CharField(max_length=30)

	partida = models.ForeignKey('auth.User', related_name="id_partida",null=True, blank=True, on_delete=models.CASCADE)

class Estilo_de_Partida(models.Model):
	jugadas = models.TextField()

	partida = models.OneToOneField(Partida, on_delete=models.CASCADE)
	tipo_estilo = models.OneToOneField(Tipo, on_delete=models.CASCADE)
	apertura = models.OneToOneField(Apertura, on_delete=models.CASCADE)