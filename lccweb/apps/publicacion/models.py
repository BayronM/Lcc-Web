from django.db import models
from apps.usuario.models import usuario,administrador
from apps.asignatura.models import asignatura
from tinymce.models import HTMLField
import datetime

YEAR_CHOICES = []
for r in range((datetime.datetime.now().year-5), (datetime.datetime.now().year+1)):
	YEAR_CHOICES.append((r,r))
# Create your models here.

class seccion(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20)
	descripcion = models.TextField()

	def __str__(self):
		return(self.nombre)


class prueba(models.Model):
	PEP_CHOICES = [
	('pep1', 'PEP 1'),
	('pep2', 'PEP 2'),
	('pep3', 'PEP 3'),
	('recuperativa', 'Recuperativa'),
	('examen', 'Examen')
	]
	nombre=models.CharField(max_length=7,choices=PEP_CHOICES,default='pep1')
	fecha=models.DateField()
	HORARIO_CHOICES = [
		(1,'Modulo 1-2 (8:00-9:30)'),
		(2,'Modulo 3-4 (9:40-11:10)'),
		(3,'Modulo 5-6 (11:20-12:50)'),
		(4,'Modulo 7-8 (13:50-15:20)'),
		(5,'Modulo 9-10 (15:30-17:00)'),
		(6,'Modulo 11-12 (17:10-18:40)'),
		(7,'Modulo 13-14 (18:45-20:10)'),
		(8,'Modulo 15-16 (20:10-21:35)'),
		(9,'Modulo 17-18 (21:35-23:00)'),
		(0,'Horario sin asignar'),
		]
	horario = models.IntegerField(
			choices=HORARIO_CHOICES,
			default=0)
	SEMESTRE_CHOICES=[
		(1,'Primer semestre'),
		(2,'Segundo semestre'),
	]
	semestre=models.IntegerField(
			choices=SEMESTRE_CHOICES,
			default='1')
	sala = models.CharField(max_length=10)
	asig = models.ForeignKey(asignatura, on_delete=models.CASCADE)

	def __str__(self):
		return ("Prueba "+self.asig.nombre)

class publicacion(models.Model):
	id = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=50)
	tags = models.CharField(max_length=30)
	imagen = models.ImageField(null=True,upload_to='imagenes/')
	fecha = models.DateField()
	seccion = models.ForeignKey(seccion(id),on_delete=models.CASCADE)
	ESTADO_CHOICES = [
		(1,'Activo (La notica sera publicada)'),
		(0,'No Activo(La noticia no estara publicada)')
	]
	estado=models.IntegerField(choices=ESTADO_CHOICES,default=0)
	CALENDARIO_CHOICES = [
		(1,'Si'),
		(0,'No')
	]
	calendarioprueba=models.IntegerField(choices=CALENDARIO_CHOICES,default=0)
	SEMESTRE_CHOICES = [
		(1,'Primer semestre '),
		(2,'Segundo semestre')
	]
	calsemestre=models.IntegerField(choices=SEMESTRE_CHOICES,default=1)
	calagno=models.IntegerField(choices=YEAR_CHOICES,default=datetime.datetime.now().year)


	def __str__(self):
		return(self.titulo);


class noticia(publicacion):
	descripcion = models.TextField()
	cuerpo = HTMLField('Content')
