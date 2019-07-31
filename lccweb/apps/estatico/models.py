from django.db import models
from tinymce.models import HTMLField

class Contenido_Estatico(models.Model):
    nombre = models.CharField(max_length=20)
    contenido = HTMLField('Content')

    def __str__(self):
        return(self.nombre)
