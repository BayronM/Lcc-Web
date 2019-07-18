from django.urls import include, path
from apps.publicacion.views  import home_view,news_view,news_view_detail,calendar_view

urlpatterns = [
    path('',home_view),
    path('noticias/<int:pub_id>/', news_view_detail),
    path('noticias/', news_view),
    path('calendario/', calendar_view)
]
