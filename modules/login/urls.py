from django.urls import path
from django.contrib.auth import views as auth_views
from .views import my_login

urlpatterns = [
    #path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('login/', my_login,name='index')
]