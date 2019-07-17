from django.db import models
from apps.usuario.models import usuario,administrador

# Create your models here.
class seccion(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20)
	descripcion = models.TextField()
<<<<<<< HEAD

	def __str__(self):
		return(self.nombre)
=======
	admin =models.ForeignKey(administrador(usuario), on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre
>>>>>>> b640d2cd0630be293c4a2c9d8707f048058c8f89
