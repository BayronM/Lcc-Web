from django.db import models
from apps.usuario.models import usuario,administrador

# Create your models here.
class seccion(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20)
	descripcion = models.TextField()
	admin =models.ForeignKey(administrador(usuario), on_delete=models.CASCADE)
