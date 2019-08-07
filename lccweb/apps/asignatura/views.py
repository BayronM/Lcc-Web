from django.shortcuts import render
from django.http import Http404
from .models import programa_estudio,asignatura
from apps.estatico.models import Contenido_Estatico
# Create your views here.
def program_view(request,*args,**kwargs):
    obj = programa_estudio.objects.order_by('año')
    asig = asignatura.objects.order_by('nivel')
    template_name="html/program.html"
    context={
    'list_of_program':obj,
    'asignaturas' : asig
    }
    return render(request,template_name,context)

def malla_view(request):
    obj = asignatura.objects.all()
    content=Contenido_Estatico.objects.all()
    template_name="html/malla.html"
    context ={
    'list_of_content' : content,
    'asignaturas' : obj,
    'range' : range(10)
    }
    return render(request,template_name,context)
