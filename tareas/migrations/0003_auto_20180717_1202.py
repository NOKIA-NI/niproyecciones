# Generated by Django 2.0.3 on 2018-07-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_auto_20180717_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='ejecutar',
            field=models.CharField(max_length=255),
        ),
    ]