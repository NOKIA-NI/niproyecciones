# Generated by Django 2.0.3 on 2018-05-21 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0013_auto_20180521_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='bolsa',
            field=models.CharField(blank=True, choices=[('', '---------'), ('55 sitios LSM', '55 sitios LSM'), ('165 sitios LSM', '165 sitios LSM'), ('170 sitios LSM', '170 sitios LSM'), ('531 sitios LSM', '531 sitios LSM'), ('Sitios Bulk', 'Sitios Bulk'), ('AIRSCALE', 'AIRSCALE'), ('AIRSCALE 240', 'AIRSCALE 240'), ('Reemplazo 170 sitios LSM', 'Reemplazo 170 sitios LSM'), ('36 sitios Satelitales LSM', '36 sitios Satelitales LSM'), ('Reemplazo 36 sitios Satelitales LSM', 'Reemplazo 36 sitios Satelitales LSM')], max_length=255, null=True),
        ),
    ]
