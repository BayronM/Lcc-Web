from django.db import models
from apps.usuario.models import usuario,administrador
from apps.programa_estudio.models import programa_estudio
from apps.seccion.models import seccion
# Create your models here.
class publicacion(models.Model):
	id = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=50)
	tags = models.CharField(max_length=30)
	fecha = models.DateField()
	admin =models.ForeignKey(administrador(usuario), on_delete=models.CASCADE)
	seccion = models.OneToOneField(seccion,on_delete=models.CASCADE)
class noticia(publicacion):
	descripcion = models.TextField()
	cuerpo = models.TextField()

class calendario_prueba(publicacion):
	fecha_prueba = models.DateField()
	horario = models.CharField(max_length=10)
	tipocalendario = models.CharField(max_length=10)
	sala = models.CharField(max_length=10)
	asig = models.ForeignKey(programa_estudio, on_delete=models.CASCADE) 
