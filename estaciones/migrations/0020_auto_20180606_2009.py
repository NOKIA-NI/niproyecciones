# Generated by Django 2.0.3 on 2018-06-07 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0019_auto_20180606_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='w_fc_c',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
