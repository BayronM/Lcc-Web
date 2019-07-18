from django.shortcuts import render , get_object_or_404
from django.http import Http404

from .models import publicacion,noticia, prueba
# Create your views here.

def home_view(request, *args,**kwargs):
    obj=publicacion.objects.all()
    template_name = "html/index.html"
    context={'list_of_publications' : obj}
    return render(request,template_name , context)


def news_view(request,*args,**kwargs):
    obj=noticia.objects.all()
    template_name = "html/news.html"
    context={'list_of_news' : obj}
    return render(request,template_name,context)



def news_view_detail(request , pub_id):
    obj = get_object_or_404(noticia, id=pub_id )
    template_name = "html/news_detail.html"
    context = { "object": obj}
    return render(request,template_name,context)

def calendar_view(request):
    obj = prueba.objects.all()
    template_name= "html/calendar.html"
    context = { 'list_of_pruebas' : obj }
    return render(request,template_name,context)
