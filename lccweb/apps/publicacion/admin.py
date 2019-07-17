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
<<<<<<< HEAD

admin.site.register(prueba)
admin.site.register(noticia,noticiaAdmin)
=======
class calendario_pruebaAdmin(admin.ModelAdmin):
    list_display = ('titulo','asig_id','fecha','seccion_id','tipocalendario','fecha_prueba','horario','sala',)
    list_filter = ('titulo','tipocalendario',)
admin.site.register(noticia,noticiaAdmin)
admin.site.register(calendario_prueba,calendario_pruebaAdmin)
>>>>>>> b640d2cd0630be293c4a2c9d8707f048058c8f89
