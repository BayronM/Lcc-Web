from django.contrib import admin
from apps.programa_estudio.models import programa_estudio
# Register your models here.
#admin.site.register(programa_estudio)
@admin.register(programa_estudio)
class Adminprograma_estudio(admin.ModelAdmin):
    list_display = ('codigo','año','semestre',)
    list_filter = ('codigo',)
    search_fields = (
        'codigo',
        'año'
    )
