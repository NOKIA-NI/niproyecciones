# Generated by Django 2.0.3 on 2018-07-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rastreos', '0007_auto_20180703_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]