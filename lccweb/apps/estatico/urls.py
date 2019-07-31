from django.urls import include, path
from apps.estatico.views  import static_view

urlpatterns = [
    path('<str:content_name>/',static_view )
]
