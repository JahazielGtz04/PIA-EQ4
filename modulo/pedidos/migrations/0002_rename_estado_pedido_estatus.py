# Generated by Django 5.1.2 on 2024-11-08 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='Estado',
            new_name='Estatus',
        ),
    ]
