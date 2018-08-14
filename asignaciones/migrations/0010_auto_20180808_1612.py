# Generated by Django 2.0.7 on 2018-08-08 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0009_auto_20180808_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitiopo',
            name='po',
        ),
        migrations.AddField(
            model_name='sitiopo',
            name='numero_po',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sitiopo',
            name='estacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
