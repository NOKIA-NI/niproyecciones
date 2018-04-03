# Generated by Django 2.0.3 on 2018-03-28 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('region', models.CharField(choices=[('Centro', 'Centro'), ('Costa', 'Costa'), ('Oriente', 'Oriente'), ('Occidente', 'Occidente'), ('Nor Oriente', 'Nor Oriente'), ('Nor Occidente', 'Nor Occidente'), ('Sur Oriente', 'Sur Oriente'), ('Sur Occidente', 'Sur Occidente')], max_length=255)),
                ('actividades', models.PositiveIntegerField(blank=True, null=True)),
                ('fc_imp', models.PositiveIntegerField(blank=True, null=True)),
                ('fc_wr', models.PositiveIntegerField(blank=True, null=True)),
                ('fc_wr_y', models.PositiveIntegerField(blank=True, null=True)),
                ('scope', models.CharField(blank=True, choices=[('', '')], max_length=255, null=True)),
                ('estado_rfe', models.CharField(blank=True, choices=[('', '')], max_length=255, null=True)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'estacion',
                'verbose_name_plural': 'estaciones',
                'ordering': ('creado',),
            },
        ),
    ]
