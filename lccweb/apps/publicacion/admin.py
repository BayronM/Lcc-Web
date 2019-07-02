from django.contrib import admin
from apps.publicacion.models import publicacion,calendario_prueba,noticia
# Register your models here.
admin.site.register(publicacion)
admin.site.register(calendario_prueba)
admin.site.register(noticia)