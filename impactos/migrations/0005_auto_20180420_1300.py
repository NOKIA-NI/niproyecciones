# Generated by Django 2.0.3 on 2018-04-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impactos', '0004_impacto_impactado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impacto',
            name='impactado',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], default='No', max_length=255, null=True),
        ),
    ]
