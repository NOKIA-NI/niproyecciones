# Generated by Django 2.0.3 on 2018-06-06 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impactos', '0010_auto_20180531_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impacto',
            name='bolsa',
            field=models.CharField(blank=True, choices=[('55 sitios LSM', '55 sitios LSM'), ('165 sitios LSM', '165 sitios LSM'), ('170 sitios LSM', '170 sitios LSM'), ('531 sitios LSM', '531 sitios LSM'), ('Sitios Bulk', 'Sitios Bulk'), ('Airscale 167', 'Airscale 167'), ('Airscale 116', 'Airscale 116'), ('Airscale 112', 'Airscale 112'), ('Reemplazo 170 sitios LSM', 'Reemplazo 170 sitios LSM'), ('36 sitios Satelitales LSM', '36 sitios Satelitales LSM'), ('Reemplazo 36 sitios Satelitales LSM', 'Reemplazo 36 sitios Satelitales LSM'), ('Partes 302 sitios LSM', 'Partes 302 sitios LSM'), ('164 Sitios LSM Mixto (Airscale + FSMF)', '164 Sitios LSM Mixto (Airscale + FSMF)')], max_length=255, null=True),
        ),
    ]
