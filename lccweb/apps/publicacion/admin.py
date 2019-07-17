from django.contrib import admin
from apps.publicacion.models import publicacion,noticia,prueba
# Register your models here.
#admin.site.register(publicacion)
#admin.site.register(calendario_prueba)
#admin.site.register(noticia)
@admin.register(publicacion)
class publicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo','tags','fecha','seccion',)
    list_filter = ('tags','seccion_id',)
class noticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha','seccion','descripcion',)
    list_filter = ('titulo','seccion_id',)

admin.site.register(prueba)
admin.site.register(noticia,noticiaAdmin)
