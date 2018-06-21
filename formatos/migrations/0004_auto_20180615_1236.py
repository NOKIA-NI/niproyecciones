# Generated by Django 2.0.3 on 2018-06-15 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0004_auto_20180516_0802'),
        ('formatos', '0003_auto_20180615_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formatoparte',
            name='parte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formatos_parte', to='partes.Parte'),
        ),
        migrations.AlterUniqueTogether(
            name='formatoparte',
            unique_together={('formato_estacion', 'parte')},
        ),
    ]