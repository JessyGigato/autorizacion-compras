from django.db import models

# Create your models here.
class Solicitud(models.Model):
    numero = models.CharField(max_length=8)
    numero_envio = models.CharField(max_length=8,blank=True,null=True)
    cod_proveedor = models.CharField(max_length=8,blank=True,null=True)
    importe_pago =  models.FloatField(blank=True,null=True)
    importe_cup = models.FloatField(blank=True,null=True)
    importe_contrato = models.FloatField(blank=True,null=True)
    moneda_contrato = models.FloatField(blank=True,null=True)
    entrega = models.CharField(max_length=20,blank=True,null=True)
    condicion_entrega =  models.CharField(max_length=3,blank=True,null=True)
    instrumento_pago = models.CharField(max_length=50,blank=True,null=True)
    facilidad_de_pago = models.CharField(max_length=50,blank=True,null=True)
    termino_pago =models.CharField(max_length=10,blank=True,null=True)
    destino = models.CharField(max_length=20,blank=True,null=True)
    fuente_pago = models.CharField(max_length=30,blank=True,null=True)
    observaciones=models.CharField(max_length=500,blank=True,null=True)
    dias_creada_enviada = models.IntegerField(blank=True,null=True)
    dias_enviada_aprobada = models.IntegerField(blank=True,null=True)
    total_dias = models.IntegerField(blank=True,null=True)
    detalle_productos_id = models.IntegerField(blank=True,null=True)
    #el tipo del campo firma_1 y firma_2 debe coincidir 
    # con el tipo del campo de la firma del firmante.
    firma_1 = models.CharField(max_length=20,blank=True,null=True) 
    firma_2 = models.CharField(max_length=20,blank=True,null=True) 


class DetalleProducto(models.Model):
    no_solicitud = models.IntegerField()
    descripcion_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField(blank=True,null=True)
    precio = models.FloatField(blank=True,null=True)
    importe = models.FloatField(blank=True,null=True)
    unidad_medida = models.CharField(max_length=20,blank=True,null=True)
    existencia = models.IntegerField(blank=True,null=True)
    ultimo_precio = models.FloatField(blank=True,null=True)

    