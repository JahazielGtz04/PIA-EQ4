# Generated by Django 5.1.2 on 2024-11-11 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_alter_pedido_fecharegistro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Contraseña',
            new_name='Contrasena',
        ),
    ]
