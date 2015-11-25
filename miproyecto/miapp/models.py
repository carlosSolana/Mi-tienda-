from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proveedor (models.Model):
	nombre = models.CharField(max_length=20)
	apellidos = models.TextField()
	seccion = models.TextField()
	

class Videojuego (models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	sinopsis =  models.TextField()
	fecha_distribucion = models.DateTimeField()
	precio = models.TextField()
	proveedor = models.ManyToManyField(Proveedor)
	usuario = models.ForeignKey(User,default=1)

	def __str__(self):
		return '%s' % (self.nombre)	


	




