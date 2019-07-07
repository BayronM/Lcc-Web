from django.urls import include, path
from apps.publicacion.views  import home_view

urlpatterns = [
    path('',home_view)
]
