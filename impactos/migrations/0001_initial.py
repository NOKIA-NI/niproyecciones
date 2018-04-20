# Generated by Django 2.0.3 on 2018-04-19 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partes', '0005_auto_20180412_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255, unique=True)),
                ('w_fc_sal', models.PositiveIntegerField(blank=True, null=True)),
                ('grupo_parte', models.CharField(blank=True, choices=[('Accesorios', 'Accesorios'), ('Modulos', 'Modulos'), ('Antenas y Otros', 'Antenas y Otros')], max_length=255, null=True)),
                ('cantidad_estimada', models.PositiveIntegerField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('parte', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='partes.Parte')),
            ],
            options={
                'verbose_name': 'impacto',
                'verbose_name_plural': 'impactos',
                'ordering': ('creado',),
            },
        ),
    ]