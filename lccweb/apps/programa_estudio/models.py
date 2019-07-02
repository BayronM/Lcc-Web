from django.db import models
from apps.asignatura.models import asignatura

# Create your models here.
class programa_estudio(models.Model):
	codigo = models.CharField(primary_key=True,max_length=5)
	año = models.IntegerField(4)
	semestre = models.IntegerField(1)
	asig = models.OneToOneField(asignatura,on_delete=models.CASCADE)
