from django.shortcuts import render
from django.http import Http404
from .models import programa_estudio,asignatura
# Create your views here.
def program_view(request,*args,**kwargs):
    obj=[programa_estudio.objects.all().order_by('codigo').order_by('año'),asignatura.objects.all().order_by('nivel')]
    template_name="html/program.html"
    context={'list_of_program':obj}
    return render(request,template_name,context)


