from django.db import models

# Create your models here.
class usuario(models.Model):
	codigo = models.CharField(max_length=10)
	rut = models.IntegerField()
	nombre = models.CharField(max_length=20)
	paterno = models.CharField(max_length=20)
	materno = models.CharField(max_length=20)
	email = models.EmailField(primary_key=True)
	contraseña = models.CharField(max_length=15)

class administrador(usuario):
	email2 = models.EmailField()
	telefono = models.CharField(max_length=10)

class estudiante(usuario):
	nivel = models.IntegerField()
	agnoing = models.DateField()