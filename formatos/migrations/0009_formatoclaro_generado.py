# Generated by Django 2.0.3 on 2018-06-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formatos', '0008_auto_20180621_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='formatoclaro',
            name='generado',
            field=models.DateField(blank=True, null=True),
        ),
    ]
