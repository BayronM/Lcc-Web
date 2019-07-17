from django.db import models

# Create your models here.
class usuario(models.Model):
    codigo = models.CharField(max_length=10)
    rut = models.IntegerField()
    nombre = models.CharField(max_length=20)
    paterno = models.CharField(max_length=20)
    materno = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True)
    contraseña = models.CharField(max_length=15)
    def __str__(self):
            return self.email
class administrador(usuario):
    email2 = models.EmailField()
    telefono = models.CharField(max_length=10)
    def __str__(self):
            return self.email2
class estudiante(usuario):
    nivel = models.IntegerField()
    agnoing = models.DateField()
    def __str__(self):
            return self.email
