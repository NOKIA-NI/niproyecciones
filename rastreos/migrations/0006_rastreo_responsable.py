# Generated by Django 2.0.3 on 2018-07-03 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('rastreos', '0005_auto_20180703_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='rastreo',
            name='responsable',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Perfil'),
        ),
    ]
