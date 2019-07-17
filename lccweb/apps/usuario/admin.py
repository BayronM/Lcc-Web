from django.contrib import admin
from apps.usuario.models import usuario,administrador,estudiante
# Register your models here.
# Register your models here.
#admin.site.register(usuario)
#admin.site.register(administrador)
#admin.site.register(estudiante)
@admin.register(usuario)
class usuarioAdmin(admin.ModelAdmin):
    list_display = ('codigo','rut','nombre','email',)
    list_filter = ('nombre',)
class administradorAdmin(admin.ModelAdmin):
    list_display = ('codigo','rut','nombre','email','email2','telefono',)
    list_filter = ('nombre','email2','telefono',)
class estudianteAdmin(admin.ModelAdmin):
    list_display = ('codigo','rut','nombre','email','nivel','agnoing',)
    list_filter = ('nivel','agnoing',)
admin.site.register(administrador,administradorAdmin)
admin.site.register(estudiante,estudianteAdmin)
