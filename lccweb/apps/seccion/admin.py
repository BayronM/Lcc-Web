from django.contrib import admin
from apps.seccion.models import seccion
# Register your models here.
#admin.site.register(seccion)
@admin.register(seccion)
class Adminseccion(admin.ModelAdmin):
    list_display = ('nombre','descripcion',)
    list_filter = ('nombre',)
