# Generated by Django 2.0.3 on 2018-04-19 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0005_auto_20180406_1517'),
        ('impactos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impacto',
            name='site_name',
        ),
        migrations.AddField(
            model_name='impacto',
            name='estacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='impactos', to='estaciones.Estacion'),
        ),
    ]
