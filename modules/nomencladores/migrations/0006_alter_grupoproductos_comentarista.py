# Generated by Django 4.1.7 on 2023-08-10 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomencladores', '0005_alter_documentoprestamista_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupoproductos',
            name='comentarista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nomencladores.comentarista'),
        ),
    ]
