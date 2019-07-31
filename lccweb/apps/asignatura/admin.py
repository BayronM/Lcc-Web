from django.contrib import admin
from apps.asignatura.models import requisito,asignatura,programa_estudio
# Register your models here.
#admin.site.register(asignatura)
@admin.register(requisito)
@admin.register(asignatura)
class Adminrequisito(admin.ModelAdmin):
    list_display = ('codasig','nombre',)
    list_filter = ('codasig','nombre',)
    search_fields = (
        'codasig',
        'nombre',
    )
class Adminasignatura(admin.ModelAdmin):
    list_display = ('codasig','nombre','nivel','semestre','requisito','plan_id')
    list_filter = ('codasig','nombre',)
    search_fields = (
        'codasig',
        'nombre',
        'nivel',
        'semestre'
    )
@admin.register(programa_estudio)
class Adminprograma_estudio(admin.ModelAdmin):
    list_display = ('codigo','año')
    list_filter = ('codigo',)
    search_fields = (
        'codigo',
    )
