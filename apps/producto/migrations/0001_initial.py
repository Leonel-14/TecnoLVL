# Generated by Django 5.1.1 on 2024-09-29 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('imagen', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=100)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.categoria')),
                ('id_estado_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.estadoproducto')),
            ],
        ),
    ]