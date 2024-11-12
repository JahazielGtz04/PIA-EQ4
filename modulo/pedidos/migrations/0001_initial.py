# Generated by Django 5.1.2 on 2024-11-07 03:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('IdUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=80)),
                ('Cuenta', models.EmailField(max_length=254, unique=True)),
                ('Contraseña', models.CharField(max_length=128)),
                ('Rol', models.CharField(choices=[('mesero', 'Mesero'), ('chef', 'Chef')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('IdPedido', models.AutoField(primary_key=True, serialize=False)),
                ('Mesa', models.IntegerField()),
                ('Platillo', models.CharField(max_length=100)),
                ('Estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado')], default='pendiente', max_length=10)),
                ('FechaRegistro', models.DateTimeField(auto_now_add=True)),
                ('UsuarioRegistro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.usuario')),
            ],
        ),
    ]
