from django.shortcuts import render, get_object_or_404
from .models import Contenido_Estatico

# Create your views here.
def static_view(request,content_name):
    obj = get_object_or_404(Contenido_Estatico,nombre=content_name)
    content=Contenido_Estatico.objects.all()
    template_name="html/static_content.html"
    context={'content' : obj,
        'list_of_content' : content }
    return render(request,template_name,context)
