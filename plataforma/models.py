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
	
	username = models.OneToOneField('auth.User', on_delete=models.CASCADE)

	def __unicode__(self):
		return self.username

class Foto(models.Model):
	ruta = models.ImageField(
		upload_to ='../imagenes/Profiles/', height_field=None, width_field=None, max_length=100)
	
	username =models.OneToOneField(Perfil, null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.username

class Direccion(models.Model):
	calle = models.CharField(max_length=30, null=True, blank=True, default=None)
	avenida = models.CharField(max_length=30, null=True, blank=True, default=None)
	cuidad = models.CharField(max_length=30, null=True, blank=True, default=None)
	pais = models.CharField(max_length=30, null=True, blank=True, default=None)

	username = models.ForeignKey(Perfil, related_name="addresses", on_delete=models.CASCADE)

	def __unicode__(self):
		return self.username

class ELO(models.Model):
	tipo = models.CharField(max_length=10, primary_key=True)
	num_win = models.IntegerField()
	num_lose = models.IntegerField()
	num_draw = models.IntegerField()

	username = models.ForeignKey(Perfil, related_name="rankings", null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.username


#Zona de clase 

class Curso(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30, null=True, blank=True, default=None)

	def __unicode__(self):
		return self.nombre

class Estudiante(models.Model):
	promedio = models.IntegerField()
	username = models.OneToOneField('auth.User', on_delete=models.CASCADE)

	def __unicode__(self):
		return self.username

class Tutor(models.Model):
	Salario = models.IntegerField()
	username = models.OneToOneField('auth.User', on_delete=models.CASCADE)

	def __unicode__(self):
		return self.username

class Seccion_De(models.Model):
	fecha_inicio =  models.DateTimeField()
	fecha_fin =  models.DateTimeField()
	costo = models.IntegerField()
	
	curso = models.ForeignKey(Curso, related_name="clase",null=True, blank=True, on_delete=models.CASCADE)

class Seccion(models.Model):
	nombre = models.CharField(max_length=30, null=True, blank=True, default=None)

	codigo = models.ForeignKey(Seccion_De,related_name ="modulo", null=True, blank=True, on_delete=models.CASCADE)
	tutor = models.ForeignKey(Tutor, related_name ="profesor", null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.nombre


class Asiste_a(models.Model):
	nota = models.IntegerField()

	seccion = models.ManyToManyField(Seccion)
	estudiante = models.ManyToManyField(Estudiante)

#Zona de Amigos

class Amigo(models.Model):
	
	aceptar = models.BooleanField(default=False)

	seguidores = models.ForeignKey('auth.User', null=True,related_name="seguidores", blank=True, on_delete=models.CASCADE)
	siguiendo = models.ForeignKey('auth.User', null=True,related_name="seguidor", blank=True, on_delete=models.CASCADE)

	class Meta:
		unique_together = ['seguidores','siguiendo']

#Zona de Partida

class Partida(models.Model):
	codigo = models.AutoField(primary_key=True)
	contrincante = models.CharField(max_length=30)
	jugadas = models.TextField()
	fecha_hora =  models.DateTimeField()
	resultado = models.CharField(max_length=30)

	usuario = models.ForeignKey('auth.User', related_name="id_partida",null=True, blank=True, on_delete=models.CASCADE)
	tipo = models.OneToOneField('Tipo', on_delete=models.CASCADE)
	apertura = models.OneToOneField('Apertura', on_delete=models.CASCADE)
	tipo = models.OneToOneField('Tipo', on_delete=models.CASCADE)

	def __unicode__(self):
		return self.contrincante
	
class Tipo(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre

class Apertura(models.Model):
	codigo = models.CharField(max_length=5, primary_key=True)
	nombre = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre

class Medio_Juego(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)

	partida = models.ForeignKey(Partida, related_name="mediojuego", null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.nombre

class Final(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)

	partida = models.ForeignKey(Partida, related_name="final", null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.nombre

class Estructura_Peones(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)
	
	partida = models.ForeignKey(Partida, related_name="estructura", null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.nombre


	