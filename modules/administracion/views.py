from django.shortcuts import render,redirect
from django.views.generic import UpdateView,ListView, CreateView
from ..usuario.models import Usuario
from .models import ConfigParametros, Entidad
from .forms import RolUsuarioForm, CreaEntidadForm,ConfigParametrosForm,AsignarUsuarioEntidadForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,JsonResponse

def get_usuario_rol(request, usuario_id):
    # Obtener el usuario por su ID
    usuario = Usuario.objects.get(id=usuario_id)

    # Devolver el rol del usuario como respuesta JSON
    return JsonResponse({'rol': usuario.rol})


nombre_rol = {
    '1':'Solicitante',
    '2':'Firmante A',
    '3':'Firmante B',
    '4':'Aprobador',
}

# Create your views here.
class RolUsuarioList(ListView):
    model = Usuario
    template_name = 'administracion/usuario_rol_list.html'

def update_params(request):
    if request.method == 'POST':
        form = ConfigParametrosForm(request.POST)
        config = ConfigParametros.load()
        if form.is_valid():
            config.limite_crear_sao = form.cleaned_data['limite_crear_sao']
            config.limite_aprobacion_division = form.cleaned_data['limite_aprobacion_division']
            config.num_aprob_sao = form.cleaned_data['num_aprob_sao']
            config.nomenclador_general = form.cleaned_data['nomenclador_general']
            config.proveedores = form.cleaned_data['proveedores']
            config.inversiones = form.cleaned_data['inversiones']
            config.sao = form.cleaned_data['sao']
            config.entidades = form.cleaned_data['entidades']
            config.save()
            return render(request,'administracion/config_params.html',{'config':config,'form':form})
    else:
        config = ConfigParametros.load()
        form = ConfigParametrosForm() 
    return render(request,'administracion/config_params.html',{'config':config,'form':form})

def asignar_rol(request):
    if request.method == 'POST':
        form = RolUsuarioForm(request.POST)
        if form.is_valid():
            seleccion = form.cleaned_data['username']
            registro = Usuario.objects.get(username=seleccion.username)
            id_rol = form.cleaned_data['rol']
            rol = nombre_rol[id_rol]
            firma = form.cleaned_data['firma']
            #Actualizo
            registro.rol = rol
            registro.firma = make_password(firma)
            registro.save()
            return redirect('administracion:lista_rol')
    else:
        form = RolUsuarioForm()
    return render(request, 'administracion/asignar_rol.html', {'form': form})

def crear_entidad(request):
    if request.method == 'POST':
        form = CreaEntidadForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('administracion:crea_entidad')
    else:
        form = CreaEntidadForm()
    return render(request, 'administracion/crear_entidad_copy.html', {'form': form})

class EntidadCreate(CreateView):
    model = Entidad
    form_class = CreaEntidadForm
    template_name = 'administracion/crear_entidad_copy.html'
    success_url = reverse_lazy('administracion:asigna_usuario_entidad')

    def get_success_url(self):
        #nombre = self.form_class.cleaned_data['nombre']
        #print('Nombre   ',nombre)
        codigo = self.object.codigo
        print('Codigo   ',codigo, type(codigo))
        return reverse_lazy('administracion:asigna_usuario_entidad',
                            kwargs={'codigo_entidad':codigo})
    
def asigna_usuario_entidad(request,codigo_entidad):
    form = AsignarUsuarioEntidadForm()
    if request.method == 'POST':
        seleccion = request.POST.get('username')
        if seleccion:
            entidad = Entidad.objects.get(codigo=codigo_entidad)
            usuario = Usuario.objects.get(username=seleccion)

            #Actualizo
            entidad.usuarios.add(usuario)
            entidad.save()

            lista_usuarios = entidad.usuarios.all()
            return render(request, 'administracion/asignar_usuario_entidad.html',
                              {'form':form,'lista_usuarios':lista_usuarios})
        
    entidad = Entidad.objects.get(codigo=codigo_entidad)

    lista_usuarios = entidad.usuarios.all()
    return render(request, 'administracion/asignar_usuario_entidad.html',
                    {'form':form,'lista_usuarios':lista_usuarios})
    #return render(request, 'administracion/asignar_usuario_entidad.html', {'form': form})

class EntidadList(ListView):
    model = Entidad
    template_name = 'administracion/lista_entidades.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Realiza la consulta para obtener los elementos de EntidadUsuario donde entidad es igual a 6
        entidades = Entidad.objects.all()
        entidad_usuario = {}
        for entidad in entidades:
            entidad_usuario[entidad.id] = entidad.usuarios.all()# .objects.filter(id=entidad.id)
            print(entidad_usuario[entidad.id])
        # Pasa los resultados al contexto
        context['entidad_usuario'] = entidad_usuario
        return context

def flujo_aprobacion():
    return

