from typing import Any, Dict
from django.shortcuts import render,redirect
from django.template.response import  TemplateResponse
from django.views.generic import CreateView, ListView
from .models import Usuario
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
class UsuarioList(ListView):
    model = Usuario
    template_name = "usuario/lista_usuarios.html"


class UsuarioCreate(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = "usuario/crear_usuario.html"
    success_url = reverse_lazy('usuario:lista_usuarios')

# class UsuarioCreate(CreateView):
#     model = Usuario
#     template_name = 'usuario/crear_usuario.html'
#     form_class = RegistroUsuarioForm
#     success_url = reverse_lazy('usuario:lista_usuarios')

#     # def post(self,request,*args,**kwargs):
#     #     print("DATAAA",request.POST['firma'])
#     #     self.object = self.get_object
#     #     form = self.form_class(request.POST)
#     #     print("FOOOORM-->",form)
#     #     if form.is_valid():
#     #         form.save(commit=False)
#     #         return HttpResponse(self.get_success_url())
#     #     else:
#     #         return render(request,'usuario/crear_usuario.html',(self.get_context_data(**kwargs)))

