# Generated by Django 2.0.3 on 2018-06-20 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0026_auto_20180619_1038'),
        ('formatos', '0004_auto_20180615_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormatoClaro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('sap', models.PositiveIntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('qty', models.PositiveIntegerField(blank=True, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=255, null=True)),
                ('regional', models.CharField(blank=True, choices=[('', '---------'), ('Centro', 'Centro'), ('Costa', 'Costa'), ('Oriente', 'Oriente'), ('Occidente', 'Occidente'), ('Nor Oriente', 'Nor Oriente'), ('Nor Occidente', 'Nor Occidente'), ('Sur Oriente', 'Sur Oriente'), ('Sur Occidente', 'Sur Occidente')], max_length=255, null=True)),
                ('semana', models.PositiveIntegerField(blank=True, null=True)),
                ('mes', models.CharField(blank=True, choices=[('ENERO', 'ENERO'), ('FEBRERO', 'FEBRERO'), ('MARZO', 'MARZO'), ('ABRIL', 'ABRIL'), ('MAYO', 'MAYO'), ('JUNIO', 'JUNIO'), ('JULIO', 'JULIO'), ('AGOSTO', 'AGOSTO'), ('SEPTIEMBRE', 'SEPTIEMBRE'), ('OCTUBRE', 'OCTUBRE'), ('NOVIEMBRE', 'NOVIEMBRE'), ('DICIEMBRE', 'DICIEMBRE')], max_length=255, null=True)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('formato_parte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_claro', to='formatos.FormatoParte')),
                ('sitio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_claro', to='estaciones.Estacion')),
            ],
            options={
                'verbose_name': 'formato claro',
                'verbose_name_plural': 'formatos claro',
                'ordering': ('creado',),
            },
        ),
    ]
