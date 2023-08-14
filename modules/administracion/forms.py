from django import forms
from ..usuario.models import Usuario
from .models import Entidad, ConfigParametros

class RolUsuarioForm(forms.Form):
    roles = [('1','Solicitante'),('2','Firmante A'),('3','Firmante B'),('4','Aprobador')]
    rol = forms.ChoiceField(widget=forms.RadioSelect(attrs={'name':"rol"}),choices=roles)
    username = forms.ModelChoiceField(queryset=Usuario.objects.all())
    firma = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Firma', 'name':"firma"}))

    class Meta:
        model = Usuario
        fields = [
            'username',
            'rol',
            'firma'
        ] 
        labels = {
            'username': 'Nombre de usuario',
            'rol': 'Rol del usuario',
            'firma': 'Firma',
        }
    
class CreaEntidadForm(forms.ModelForm):
    #nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'name':"nombre"}))
    #codigo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Código','name':'codigo'}))
    #usuarios = forms.ModelChoiceField(queryset=Usuario.objects.all())

    class Meta:
        model = Entidad
        fields = [
            'nombre',
            'codigo',
            #'usuarios'
        ] 
        labels = {
            'nombre': 'Nombre de entidad',
            'codigo': 'Código de entidad',
            #'usuarios': 'Usuarios',
        }

class AsignarUsuarioEntidadForm(forms.ModelForm):
    usuarios = forms.ModelChoiceField(queryset=Usuario.objects.all())

    class Meta:
        model = Entidad
        fields = [
            #'nombre',
            #'codigo',
            'usuarios'
        ] 
        labels = {
            #'nombre': 'Nombre de entidad',
            #'codigo': 'Código de entidad',
            'usuarios': 'Usuarios',
        }

class ConfigParametrosForm(forms.ModelForm):
    
    class Meta:
        model = ConfigParametros

        fields = [
            'limite_crear_sao',
            'limite_aprobacion_division',
            'num_aprob_sao',
            'nomenclador_general',
            'proveedores',
            'inversiones',
            'sao',
            'entidades',
        ] 
        labels = {
            'limite_crear_sao' : 'Limite para crear SAO(USD)',
            'limite_aprobacion_division': 'Limite Aprobacion División',
            'num_aprob_sao': 'Número de Aprobación SAO(<10000)',
            'nomenclador_general': 'Nomenclador general',
            'proveedores': 'Provedores',
            'inversiones': 'Inversiones',
            'sao': 'SAO',
            'entidades': 'Entidades',
        }