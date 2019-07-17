from django.contrib import admin
from apps.asignatura.models import asignatura
# Register your models here.
#admin.site.register(asignatura)

@admin.register(asignatura)
class Adminasignatura(admin.ModelAdmin):
    list_display = ('codasig','nombre','requisito',)
    list_filter = ('codasig','nombre',)
