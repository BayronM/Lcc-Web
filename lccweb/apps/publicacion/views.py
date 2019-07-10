from django.shortcuts import render , get_object_or_404
from django.http import Http404

from .models import publicacion,noticia
# Create your views here.

def home_view(request, *args,**kwargs):
    obj=publicacion.objects.all()
    context={'list_of_publications' : obj}
    return render(request,"HTML/index.html", context)


def news_view(request,*args,**kwargs):
    obj=noticia.objects.all()
    context={'list_of_news' : obj}
    return render(request,"HTML/news.html",context)



def news_view_detail(request , pub_id):
    obj = get_object_or_404(noticia, id=pub_id )
    context = { "object": obj}
    return render(request,"HTML/news_detail.html",context)
