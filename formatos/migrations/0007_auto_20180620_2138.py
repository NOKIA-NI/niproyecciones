# Generated by Django 2.0.3 on 2018-06-21 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formatos', '0006_auto_20180620_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formatoclaro',
            name='formato_parte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_claro', to='formatos.FormatoParte'),
        ),
    ]
