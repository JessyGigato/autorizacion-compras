from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class RolUsuarioForm(forms.ModelForm):
    roles = [('1','Solicitante'),('2','Firmante A'),('3','Firmante B'),('4','Aprobador')]
    rol = forms.ChoiceField(widget=forms.RadioSelect(attrs={'name':"rol"}),choices=roles)

    class Meta:
        model = Usuario
        fields = [
            'rol',
            'firma'
        ] 
        labels = {
            'rol': 'Rol del usuario',
            'firma': 'Firma',
        }
    
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     if self.cleaned_data['firma']:
    #         instance.firma = make_password(self.cleaned_data['firma'])
    #     if commit:
    #         instance.save()
    #     return instance

class RegistroUsuarioForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'first name': 'Nombre',
            'last name': 'Apellidos',
            'email': 'Email',
            'password1':'Contraseña',
            'password2':'Repite la ontraseña',

        }        
        

        
