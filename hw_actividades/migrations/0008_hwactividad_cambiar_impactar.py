# Generated by Django 2.0.3 on 2018-05-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_actividades', '0007_auto_20180515_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='hwactividad',
            name='cambiar_impactar',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], max_length=255, null=True),
        ),
    ]
