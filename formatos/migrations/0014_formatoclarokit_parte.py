# Generated by Django 2.0.3 on 2018-06-27 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0004_auto_20180516_0802'),
        ('formatos', '0013_formatoclarokit'),
    ]

    operations = [
        migrations.AddField(
            model_name='formatoclarokit',
            name='parte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_claro_kit', to='partes.Parte'),
        ),
    ]
