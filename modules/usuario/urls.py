from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, UsuarioList

urlpatterns = [
    path('', UsuarioList.as_view(),name='lista_usuarios'),
    path('crear/', UsuarioCreate.as_view(), name='crea_usuarios')
]