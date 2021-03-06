# Generated by Django 2.0.3 on 2018-07-18 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0029_auto_20180710_1048'),
        ('partes', '0004_auto_20180516_0802'),
        ('formatos', '0014_formatoclarokit_parte'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormatoParteDelta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_parte', models.PositiveIntegerField(blank=True, null=True)),
                ('cantidad_input', models.PositiveIntegerField(blank=True, null=True)),
                ('cantidad_delta', models.PositiveIntegerField(blank=True, null=True)),
                ('fecha_delta', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_parte_delta', to='estaciones.Estacion')),
                ('parte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_parte_delta', to='partes.Parte')),
            ],
            options={
                'verbose_name': 'formato parte delta',
                'verbose_name_plural': 'formatos parte delta',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='FormatoParteInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_parte_input', to='estaciones.Estacion')),
                ('parte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_parte_input', to='partes.Parte')),
            ],
            options={
                'verbose_name': 'formato parte input',
                'verbose_name_plural': 'formatos parte input',
                'ordering': ('creado',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='formatoparteinput',
            unique_together={('estacion', 'parte')},
        ),
        migrations.AlterUniqueTogether(
            name='formatopartedelta',
            unique_together={('estacion', 'parte')},
        ),
    ]
