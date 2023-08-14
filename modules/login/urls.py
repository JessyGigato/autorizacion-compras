from django.urls import path
from django.contrib.auth import views as auth_views
from .views import my_login, index_

urlpatterns = [
    #path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('', my_login,name='index_login'),
    path('index/',index_,name='index'),
]