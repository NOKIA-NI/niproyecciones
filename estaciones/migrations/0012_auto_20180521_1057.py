# Generated by Django 2.0.3 on 2018-05-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0011_estacion_partes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='partes',
            field=models.ManyToManyField(blank=True, to='partes.Parte'),
        ),
    ]
