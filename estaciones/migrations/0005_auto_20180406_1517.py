# Generated by Django 2.0.3 on 2018-04-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0004_auto_20180406_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='bolsa',
            field=models.CharField(blank=True, choices=[('', '---------'), ('45 sitios LSM', '45 sitios LSM'), ('120 sitios LSM', '120 sitios LSM'), ('128 sitios LSM', '128 sitios LSM'), ('485 sitios', '485 sitios'), ('531 sitios LSM', '531 sitios LSM'), ('Reemplazo 531', 'Reemplazo 531'), ('Sitios Bulk', 'Sitios Bulk')], max_length=255, null=True),
        ),
    ]
