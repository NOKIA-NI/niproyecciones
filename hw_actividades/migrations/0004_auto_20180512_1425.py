# Generated by Django 2.0.3 on 2018-05-12 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hw_actividades', '0003_hwactividad_proyeccion_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hwactividad',
            name='proyeccion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proyecciones.Proyeccion'),
        ),
    ]