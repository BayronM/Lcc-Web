from django.shortcuts import render
from django.http import HttpResponse

from .models import publicacion
# Create your views here.

def home_view(request, *args,**kwargs):
    return render(request,"index.html",{})
