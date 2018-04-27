# Generated by Django 2.0.3 on 2018-04-27 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Existencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo_parte', models.CharField(blank=True, choices=[('Accesorios', 'Accesorios'), ('Modulos', 'Modulos'), ('Antenas y Otros', 'Antenas y Otros')], max_length=255, null=True)),
                ('w14', models.IntegerField(default=0)),
                ('w15', models.IntegerField(default=0)),
                ('w16', models.IntegerField(default=0)),
                ('w17', models.IntegerField(default=0)),
                ('w18', models.IntegerField(default=0)),
                ('w19', models.IntegerField(default=0)),
                ('w20', models.IntegerField(default=0)),
                ('w21', models.IntegerField(default=0)),
                ('w22', models.IntegerField(default=0)),
                ('w23', models.IntegerField(default=0)),
                ('w24', models.IntegerField(default=0)),
                ('w25', models.IntegerField(default=0)),
                ('w26', models.IntegerField(default=0)),
                ('w27', models.IntegerField(default=0)),
                ('w28', models.IntegerField(default=0)),
                ('w29', models.IntegerField(default=0)),
                ('w30', models.IntegerField(default=0)),
                ('w31', models.IntegerField(default=0)),
                ('w32', models.IntegerField(default=0)),
                ('w33', models.IntegerField(default=0)),
                ('w34', models.IntegerField(default=0)),
                ('w35', models.IntegerField(default=0)),
                ('w36', models.IntegerField(default=0)),
                ('w37', models.IntegerField(default=0)),
                ('w38', models.IntegerField(default=0)),
                ('w39', models.IntegerField(default=0)),
                ('w40', models.IntegerField(default=0)),
                ('w41', models.IntegerField(default=0)),
                ('w42', models.IntegerField(default=0)),
                ('w43', models.IntegerField(default=0)),
                ('w44', models.IntegerField(default=0)),
                ('w45', models.IntegerField(default=0)),
                ('w46', models.IntegerField(default=0)),
                ('w47', models.IntegerField(default=0)),
                ('w48', models.IntegerField(default=0)),
                ('w49', models.IntegerField(default=0)),
                ('w50', models.IntegerField(default=0)),
                ('w51', models.IntegerField(default=0)),
                ('w52', models.IntegerField(default=0)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('parte', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='partes.Parte')),
            ],
            options={
                'verbose_name': 'existencia',
                'verbose_name_plural': 'existencias',
                'ordering': ('creado',),
            },
        ),
    ]
