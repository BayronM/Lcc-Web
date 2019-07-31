from django.shortcuts import render , get_object_or_404
from django.http import Http404

from .models import publicacion,noticia, prueba
from apps.estatico.models import Contenido_Estatico
# Create your views here.

def home_view(request, *args,**kwargs):
    obj=publicacion.objects.order_by('-fecha').filter(estado=1)[:9]
    content=Contenido_Estatico.objects.all()
    template_name = "html/index.html"
    context={'list_of_publications' : obj,
            'list_of_content' : content }
    return render(request,template_name , context)


def news_view(request,*args,**kwargs):
    obj=noticia.objects.order_by('-fecha').filter(estado=1)[:9]
    content=Contenido_Estatico.objects.all()
    template_name = "html/news.html"
    context={'list_of_news' : obj,
    'list_of_content' : content }
    return render(request,template_name,context)



def news_view_detail(request , pub_id):
    obj = get_object_or_404(publicacion, id=pub_id )
    objprueba=prueba.objects.filter(semestre=obj.calsemestre
                                    ,fecha__year=obj.calagno)
    template_name = "html/news_detail.html"
    context = { "object": obj,
               "Pruebas": objprueba,
               'list_of_content' : content }
    return render(request,template_name,context)

def calendar_view(request):
    obj = prueba.objects.all()
    template_name= "html/calendar.html"
    context = { 'list_of_pruebas' : obj }
    return render(request,template_name,context)
