# Generated by Django 2.0.7 on 2018-08-01 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0004_auto_20180731_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacionantena',
            name='comentario_bodega',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='asignacionantena',
            name='po',
            field=models.CharField(blank=True, default='Bulk', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='asignacionantena',
            name='so',
            field=models.CharField(blank=True, default='Bulk', max_length=255, null=True),
        ),
    ]
