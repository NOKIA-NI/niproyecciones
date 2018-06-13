# Generated by Django 2.0.3 on 2018-06-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0021_auto_20180607_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='bolsa',
            field=models.CharField(blank=True, choices=[('55 sitios LSM', '55 sitios LSM'), ('165 sitios LSM', '165 sitios LSM'), ('170 sitios LSM', '170 sitios LSM'), ('531 sitios LSM', '531 sitios LSM'), ('Sitios Bulk', 'Sitios Bulk'), ('Airscale 167', 'Airscale 167'), ('381 sitios LSM Mixto (Airscale + FSMF)', '381 sitios LSM Mixto (Airscale + FSMF)'), ('114 sitios LSM Mixto (Airscale + FSMF)', '114 sitios LSM Mixto (Airscale + FSMF)'), ('Reemplazo 170 sitios LSM', 'Reemplazo 170 sitios LSM'), ('36 sitios Satelitales LSM', '36 sitios Satelitales LSM'), ('Reemplazo 36 sitios Satelitales LSM', 'Reemplazo 36 sitios Satelitales LSM'), ('Partes 302 sitios LSM', 'Partes 302 sitios LSM'), ('Pendiente Pedido', 'Pendiente Pedido')], max_length=255, null=True),
        ),
    ]
