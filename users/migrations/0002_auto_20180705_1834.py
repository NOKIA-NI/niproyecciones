# Generated by Django 2.0.3 on 2018-07-05 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'ordering': ('-creado',), 'permissions': (('perm_ni_administrador', 'Permisos para NI Administrador'), ('perm_ni_visitante', 'Permisos para NI Visitante'), ('perm_ni_rastreo', 'Permisos para NI Rastreo'), ('perm_ni_proceso', 'Permisos para NI Proceso')), 'verbose_name': 'perfil', 'verbose_name_plural': 'perfiles'},
        ),
        migrations.AlterField(
            model_name='perfil',
            name='perfil',
            field=models.CharField(blank=True, choices=[('NI Administrador', 'NI Administrador'), ('NI Visitante', 'NI Visitante'), ('NI Rastreo', 'NI Rastreo'), ('NI Proceso', 'NI Proceso')], max_length=255, null=True),
        ),
    ]
