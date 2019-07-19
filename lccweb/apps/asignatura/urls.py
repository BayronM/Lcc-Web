from django.urls import include, path
from apps.asignatura.views  import program_view

urlpatterns = [
    path('program/', program_view)
]
