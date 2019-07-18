from django.contrib import admin
from apps.publicacion.models import prueba,publicacion,noticia
# Register your models here.
#admin.site.register(publicacion)
#admin.site.register(calendario_prueba)
#admin.site.register(noticia)
@admin.register(prueba)
class pruebaAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha','horario','semestre','sala','asig_id')
    list_filter = ('asig_id','nombre')
    search_fields = (
        'nombre',
        'fecha',
        'semestre',
        'asig_id',
    )
@admin.register(publicacion)
class publicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo','tags','fecha','seccion',)
    list_filter = ('tags','seccion_id',)
    search_fields = (
        'titulo',
        'fecha',
        'tags'
    )
class noticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha','seccion','descripcion',)
    list_filter = ('titulo','seccion_id',)
    search_fields = (
        'titulo',
        'fecha'
    )
admin.site.register(noticia,noticiaAdmin)
