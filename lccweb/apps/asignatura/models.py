from django.db import models
from apps.usuario.models import usuario,administrador
# Create your models here.
class asignatura(models.Model):
	codasig = models.CharField(primary_key=True,max_length=10)
	nombre = models.CharField(max_length=20)
	areacon = models.CharField(max_length=30)
	horatel = models.CharField(max_length=15)
	sct = models.IntegerField()
	requisito = models.CharField(max_length=50)
	admin =models.ForeignKey(administrador(usuario), on_delete=models.CASCADE)
	def __str__(self):
		return self.codasig