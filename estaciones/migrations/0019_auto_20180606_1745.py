# Generated by Django 2.0.3 on 2018-06-06 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0018_auto_20180606_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estacion',
            old_name='scope_c',
            new_name='w_fc_c',
        ),
    ]