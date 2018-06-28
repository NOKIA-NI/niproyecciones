# Generated by Django 2.0.3 on 2018-06-27 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0028_auto_20180622_1728'),
        ('formatos', '0012_formatoclarototal'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormatoClaroKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sitio', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('sap', models.PositiveIntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('qty', models.PositiveIntegerField(blank=True, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=255, null=True)),
                ('regional', models.CharField(blank=True, choices=[('', '---------'), ('Centro', 'Centro'), ('Costa', 'Costa'), ('Oriente', 'Oriente'), ('Occidente', 'Occidente'), ('Nor Oriente', 'Nor Oriente'), ('Nor Occidente', 'Nor Occidente'), ('Sur Oriente', 'Sur Oriente'), ('Sur Occidente', 'Sur Occidente')], max_length=255, null=True)),
                ('semana', models.PositiveIntegerField(blank=True, null=True)),
                ('mes', models.CharField(blank=True, choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=255, null=True)),
                ('generado', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('sitio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_claro_kit', to='estaciones.Estacion')),
            ],
            options={
                'verbose_name': 'formato claro kit',
                'verbose_name_plural': 'formatos claro kit',
                'ordering': ('creado',),
            },
        ),
    ]
