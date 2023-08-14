from django.db import models
from modules.usuario.models import Usuario
from django.contrib.postgres.fields import ArrayField

class Moneda(models.Model):
    siglas = models.CharField(max_length=3)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.siglas}'

class Comentarista(models.Model):
    certificado = models.CharField(max_length=30)
    nombre = models.ForeignKey(Usuario, null=True, blank=True,on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class LineaFinanciamiento(models.Model):
    codigo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    activa = models.BooleanField(default=False)
    moneda = models.ForeignKey(Moneda, null=True, blank=True,on_delete=models.CASCADE)
    expira = models.DateField()
    instrumento_pago = models.CharField(max_length=30)
    monto_financiamiento = models.FloatField()
    dias_revolvencia = models.CharField(max_length=100)
    monto_total = models.FloatField()
    dias = models.CharField(max_length=100)
    interes = models.CharField(max_length=100)
    revisa = models.BooleanField()

class InstrumentoPago(models.Model):
    codigo = models.CharField(max_length=3)
    nombre =models.CharField(max_length=30)

    def __str__(self):
        return f'{self.codigo}-{self.nombre}'

class CondicionEntrega(models.Model):
    codigo = models.CharField(max_length=3)
    nombre =models.CharField(max_length=10)

class DocumentoPago(models.Model):
    codigo = models.CharField(max_length=3)
    nombre =models.CharField(max_length=30)

class DocumentoPrestamista(models.Model):
    codigo = models.CharField(max_length=2)
    nombre =models.CharField(max_length=100)

class GrupoProductos(models.Model):
    division_familia = models.CharField(max_length=50)
    descripcion =models.CharField(max_length=100)
    comentarista = models.ForeignKey(Comentarista, null=True, blank=True,on_delete=models.CASCADE)
    division_pertenecia = models.CharField(max_length=50)
    productos = ArrayField(models.TextField())

class Aerolinea(models.Model):
    codigo = models.CharField(max_length=3)
    nombre =models.CharField(max_length=30)

class AeropuertoEmbarque(models.Model):
    codigo = models.CharField(max_length=3)
    nombre =models.CharField(max_length=30)

class AgenteCarga(models.Model):
    codigo = models.CharField(max_length=3)
    nombre =models.CharField(max_length=30)

class AlmacenDestino(models.Model):
    codigo = models.CharField(max_length=3)
    nombre =models.CharField(max_length=30)

class Naviera(models.Model):
    codigo = models.CharField(max_length=3)
    nombre =models.CharField(max_length=30)

class PuertoEmbarque(models.Model):
    codigo = models.CharField(max_length=20)
    nombre =models.CharField(max_length=30)


class Transitaria(models.Model):
    codigo = models.CharField(max_length=3)
    nombre =models.CharField(max_length=30)