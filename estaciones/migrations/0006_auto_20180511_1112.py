# Generated by Django 2.0.3 on 2018-05-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0005_auto_20180511_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='bolsa',
            field=models.CharField(blank=True, choices=[('', '---------'), ('55 sitios LSM', '55 sitios LSM'), ('165 sitios LSM', '165 sitios LSM'), ('170 sitios LSM', '170 sitios LSM'), ('485 sitios', '485 sitios'), ('531 sitios LSM', '531 sitios LSM'), ('Reemplazo 531', 'Reemplazo 531'), ('Sitios Bulk', 'Sitios Bulk'), ('AIRSCALE', 'AIRSCALE')], max_length=255, null=True),
        ),
    ]
