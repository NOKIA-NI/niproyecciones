# Generated by Django 2.0.7 on 2018-08-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0004_auto_20180516_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='grupo_parte',
            field=models.CharField(blank=True, choices=[('', '---------'), ('Accesorios', 'Accesorios'), ('Modulos', 'Modulos'), ('Antenas', 'Antenas')], max_length=255, null=True),
        ),
    ]
