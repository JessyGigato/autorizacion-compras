# Generated by Django 4.1.7 on 2023-07-08 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_solicitud', models.IntegerField()),
                ('descripcion_producto', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('importe', models.FloatField(blank=True, null=True)),
                ('unidad_medida', models.CharField(blank=True, max_length=20, null=True)),
                ('existencia', models.IntegerField(blank=True, null=True)),
                ('ultimo_precio', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=8)),
                ('numero_envio', models.CharField(blank=True, max_length=8, null=True)),
                ('cod_proveedor', models.CharField(blank=True, max_length=8, null=True)),
                ('importe_pago', models.FloatField(blank=True, null=True)),
                ('importe_cup', models.FloatField(blank=True, null=True)),
                ('importe_contrato', models.FloatField(blank=True, null=True)),
                ('moneda_contrato', models.FloatField(blank=True, null=True)),
                ('entrega', models.CharField(blank=True, max_length=20, null=True)),
                ('condicion_entrega', models.CharField(blank=True, max_length=3, null=True)),
                ('instrumento_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('facilidad_de_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('termino_pago', models.CharField(blank=True, max_length=10, null=True)),
                ('destino', models.CharField(blank=True, max_length=20, null=True)),
                ('fuente_pago', models.CharField(blank=True, max_length=30, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=500, null=True)),
                ('dias_creada_enviada', models.IntegerField(blank=True, null=True)),
                ('dias_enviada_aprobada', models.IntegerField(blank=True, null=True)),
                ('total_dias', models.IntegerField(blank=True, null=True)),
                ('detalle_productos_id', models.IntegerField(blank=True, null=True)),
                ('firma_1', models.CharField(blank=True, max_length=20, null=True)),
                ('firma_2', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
