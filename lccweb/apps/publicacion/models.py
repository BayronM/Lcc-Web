from django.db import models
from apps.usuario.models import usuario,administrador
from apps.programa_estudio.models import programa_estudio
from apps.seccion.models import seccion
# Create your models here.
class publicacion(models.Model):
	id = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=50)
	tags = models.CharField(max_length=30)
	imagen = models.ImageField(null=True,upload_to='imagenes/')
	fecha = models.DateField()
	admin =models.ForeignKey(administrador(usuario), on_delete=models.CASCADE)
	seccion = models.ForeignKey(seccion(id),on_delete=models.CASCADE)
	def __str__(self):
		return self.titulo

class noticia(publicacion):
	descripcion = models.TextField()
	cuerpo = models.TextField()
	def __str__(self):	
		return self.titulo

class calendario_prueba(publicacion):
	fecha_prueba = models.DateField()
	horario = models.CharField(max_length=10)
	tipocalendario = models.CharField(max_length=10)
	sala = models.CharField(max_length=10)
	asig = models.ForeignKey(programa_estudio, on_delete=models.CASCADE)
	def __str__(self):
		return self.titulo
