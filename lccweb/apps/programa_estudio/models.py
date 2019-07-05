from django.db import models
from apps.asignatura.models import asignatura

# Create your models here.
class programa_estudio(models.Model):
	codigo = models.CharField(primary_key=True,max_length=5)
	anno = models.IntegerField()
	semestre = models.IntegerField()
	asig = models.OneToOneField(asignatura,on_delete=models.CASCADE)
