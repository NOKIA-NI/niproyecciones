# Generated by Django 2.0.3 on 2018-06-14 23:36

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_auto_20180531_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, null=True),
        ),
    ]
