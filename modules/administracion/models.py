from django.db import models
from django.contrib.auth.models import User
from ..usuario.models import Usuario
from typing import Any
#from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Entidad(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=128)
    #usuarios = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)  
    usuarios = models.ManyToManyField(Usuario,related_name='usuarios_entidad')
    

class ConfigParametros(models.Model):
    limite_crear_sao = models.IntegerField(blank=True,null=True)
    limite_aprobacion_division = models.IntegerField(blank=True,null=True)
    num_aprob_sao = models.CharField(max_length=50,blank=True,null=True)
    nomenclador_general = models.CharField(max_length=50,blank=True)
    proveedores = models.CharField(max_length=50,blank=True)
    inversiones = models.CharField(max_length=50,blank=True)
    sao = models.CharField(max_length=50,blank=True)
    entidades = models.CharField(max_length=50,blank=True)

    def save(self, *args, **kwargs):  # type: ignore
        """Save object to the database. All other entries, if any, are removed."""
        self.__class__.objects.exclude(id=self.id).delete()
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls) -> Any:
        """Load the model instance."""
        obj, _ = cls.objects.get_or_create(id=1)
        return obj

class Condicion(models.Model):
    campo = models.CharField(max_length=30)
    comparacion = models.CharField(max_length=30)
    valor = models.CharField(max_length=30)
    siguiente = models.OneToOneField(Usuario,on_delete=models.CASCADE)

class PerfilAprobador(models.Model):
    usuario = models.OneToOneField(Usuario,related_name='usuario_aprobador',on_delete=models.CASCADE)
    sustituto = models.OneToOneField(Usuario,related_name='usuario_sustituto',on_delete=models.CASCADE)
    notificar_a = models.EmailField()
    condicion = models.ForeignKey(Condicion, on_delete=models.CASCADE)


    


     

