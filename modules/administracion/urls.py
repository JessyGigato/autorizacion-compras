from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import *# asignar_rol, RolUsuarioList, crear_entidad,update_params, get_usuario_rol

urlpatterns = [
    path('asignar_rol/', asignar_rol,name='asigna_rol'),
    path('lista_rol/',RolUsuarioList.as_view(),name='lista_rol'),
    path('crear_entidad/',  EntidadCreate.as_view(),name='crea_entidad'),
    path('parametros/',update_params,name='config_params'),
    path('get_usuario_rol/<int:usuario_id>/', get_usuario_rol, name='get_usuario_rol'),
    #path('flujo_aprobacion/',)
    path('asigna_usuario_entidad/<int:codigo_entidad>',asigna_usuario_entidad,name="asigna_usuario_entidad"),
    path('lista_entidades/', EntidadList.as_view(),name="lista_entidades"),    
    
]