# Generated by Django 2.0.3 on 2018-06-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rastreos', '0002_auto_20180629_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='procesos/archivos/'),
        ),
    ]