# Generated by Django 2.0.3 on 2018-07-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formatos', '0015_auto_20180718_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formatopartedelta',
            old_name='fecha_delta',
            new_name='fecha_formato',
        ),
        migrations.AddField(
            model_name='formatoparteinput',
            name='fecha_formato',
            field=models.DateField(blank=True, null=True),
        ),
    ]
