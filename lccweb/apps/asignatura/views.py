from django.shortcuts import render
from django.http import Http404
from .models import programa_estudio,asignatura
# Create your views here.
def program_view(request,*args,**kwargs):
    obj=[programa_estudio.objects.all().order_by('codigo'),programa_estudio.objects.all().order_by('semestre'),asignatura.objects.all()]
    template_name="html/program.html"
    context={'list_of_program':obj}
    return render(request,template_name,context)


