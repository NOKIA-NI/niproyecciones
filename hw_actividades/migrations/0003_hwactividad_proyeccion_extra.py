# Generated by Django 2.0.3 on 2018-05-11 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecciones', '0004_proyeccionextra'),
        ('hw_actividades', '0002_auto_20180503_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='hwactividad',
            name='proyeccion_extra',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecciones.ProyeccionExtra'),
        ),
    ]
