# Generated by Django 2.0.3 on 2018-07-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formatos', '0016_auto_20180719_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formatoparteinput',
            name='fecha_formato',
            field=models.DateField(),
        ),
    ]
