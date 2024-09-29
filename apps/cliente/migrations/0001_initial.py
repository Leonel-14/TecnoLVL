# Generated by Django 5.1.1 on 2024-09-29 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ubicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('calle', models.CharField(max_length=40)),
                ('altura', models.IntegerField()),
                ('piso', models.IntegerField()),
                ('departamento', models.CharField(max_length=3)),
                ('codigo_postal', models.IntegerField()),
                ('id_barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.barrio')),
            ],
        ),
    ]
