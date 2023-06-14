from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.template.response import  TemplateResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    s = request.GET['username'] + '  ' + request.GET['password'] 
    return HttpResponse(s)

@csrf_protect
def my_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('ya se ha logueado')
        else:
            return HttpResponse('Usuario Invalido')
    else:
        print('hola')
        form = AuthenticationForm(request)

    context = {
        'form': form,
    }

    return TemplateResponse(request, 'login.html', context)
