# Generated by Django 2.0.3 on 2018-04-05 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecciones', '0002_auto_20180404_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyeccion',
            name='estado_proyeccion',
            field=models.CharField(choices=[('Aprobado', 'Aprobado'), ('No Aprobado', 'No Aprobado')], max_length=255),
        ),
    ]