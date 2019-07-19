from django.contrib import admin
from apps.asignatura.models import asignatura,programa_estudio
# Register your models here.
#admin.site.register(asignatura)

@admin.register(asignatura)
class Adminasignatura(admin.ModelAdmin):
    list_display = ('codasig','nombre','requisito',)
    list_filter = ('codasig','nombre',)
    search_fields = (
        'codasig',
        'nombre',
    )
@admin.register(programa_estudio)
class Adminprograma_estudio(admin.ModelAdmin):
    list_display = ('codigo','año','semestre','asig_id')
    list_filter = ('codigo',)
    search_fields = (
        'codigo',
        'año'
    )
