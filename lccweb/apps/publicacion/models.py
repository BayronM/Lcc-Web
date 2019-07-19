from django.db import models
from apps.usuario.models import usuario,administrador
from apps.asignatura.models import asignatura
from apps.seccion.models import seccion
from tinymce.models import HTMLField
# Create your models here.

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
	modulo1_2='1'
	modulo3_4='2'
	modulo5_6='3'
	modulo7_8='4'
	modulo9_10='5'
	modulo11_12='6'
	modulo13_14='7'
	modulo15_16='8'
	modulo17_18='9'
	sinasignar='0'
	HORARIO_CHOICES = [
		(modulo1_2,'Modulo 1-2 (8:00-9:30)'),
		(modulo3_4,'Modulo 3-4 (9:40-11:10)'),
		(modulo5_6,'Modulo 5-6 (11:20-12:50)'),
		(modulo7_8,'Modulo 7-8 (13:50-15:20)'),
		(modulo9_10,'Modulo 9-10 (15:30-17:00)'),
		(modulo11_12,'Modulo 11-12 (17:10-18:40)'),
		(modulo13_14,'Modulo 13-14 (18:45-20:10)'),
		(modulo15_16,'Modulo 15-16 (20:10-21:35)'),
		(modulo17_18,'Modulo 17-18 (21:35-23:00)'),
		(sinasignar,'Horario sin asignar'),
		]
	horario = models.CharField(max_length=6,
			choices=HORARIO_CHOICES,
			default=sinasignar)
	SEMESTRE_CHOICES=[
		('1','Primer semestre'),
		('2','Segundo semestre'),
	]
	semestre=models.CharField(max_length=1,
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
	CALENDARIO_CHOICES = [
		(1,'Si'),
		(0,'No')
	]
	calendarioprueba=models.IntegerField(choices=CALENDARIO_CHOICES,default=0)

	def __str__(self):
		return(self.titulo);


class noticia(publicacion):
	descripcion = models.TextField()
	cuerpo = HTMLField('Content')
