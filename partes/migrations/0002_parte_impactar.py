# Generated by Django 2.0.3 on 2018-05-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parte',
            name='impactar',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=255),
        ),
    ]
