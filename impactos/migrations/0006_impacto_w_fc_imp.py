# Generated by Django 2.0.3 on 2018-04-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impactos', '0005_auto_20180420_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='impacto',
            name='w_fc_imp',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
