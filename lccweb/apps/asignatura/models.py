from django.db import models
# Create your models here.

class programa_estudio(models.Model):
	codigo = models.CharField(max_length=5,primary_key=True,default='0')
	año = models.IntegerField()

	def __str__(self):
		return self.codigo

class asignatura(models.Model):
	codasig = models.CharField(primary_key=True,max_length=10)
	nombre = models.CharField(max_length=20)
	areacon = models.CharField(max_length=30)
	horatel = models.CharField(max_length=15)
	sct = models.IntegerField()
	NIVEL_OPC = [
			(1,'01'),
			(2,'02'),
			(3,'03'),
			(4,'04'),
			(5,'05'),
			(6,'06'),
			(7,'07'),
			(8,'08'),
			(9,'09'),
			(10,'10')]
	nivel = models.IntegerField(choices=NIVEL_OPC,default=1)
	plan = models.ForeignKey(programa_estudio, on_delete=models.CASCADE)
	requisito = models.ManyToManyField('self',blank=True)

	def __str__(self):
		return(self.nombre)
