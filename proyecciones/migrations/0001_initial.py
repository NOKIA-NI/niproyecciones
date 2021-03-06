# Generated by Django 2.0.3 on 2018-04-27 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partes', '0001_initial'),
        ('estaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyeccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hw_proyeccion', models.IntegerField(blank=True, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('agrupadores', models.CharField(blank=True, max_length=255, null=True)),
                ('rfe', models.DateField(blank=True, null=True)),
                ('estado_proyeccion', models.CharField(choices=[('Aprobado', 'Aprobado'), ('No Aprobado', 'No Aprobado')], max_length=255)),
                ('cantidad_estimada', models.PositiveIntegerField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('estacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecciones', to='estaciones.Estacion')),
                ('parte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyecciones', to='partes.Parte')),
            ],
            options={
                'verbose_name': 'proyeccion',
                'verbose_name_plural': 'proyecciones',
                'ordering': ('creado',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='proyeccion',
            unique_together={('id', 'hw_proyeccion')},
        ),
    ]
