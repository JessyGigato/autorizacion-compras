"""autorizacion_compras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from modules.login import urls as login_url
from modules.usuario import urls as usuarios_url
from modules.administracion import urls as administracion_urls
from modules.nomencladores import urls as nomencladores_urls
from modules.login.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(login_url),name='login'),
    path('usuario/',include((usuarios_url,'usuario'),namespace='usuario'),name='usuario'),
    path('administracion/',include((administracion_urls,'administracion'),namespace='administracion'),name='administracion'),
    path('nomencladores/',include((nomencladores_urls,'nomencladores'),namespace='nomencladores'),name='nomencladores'),
]
