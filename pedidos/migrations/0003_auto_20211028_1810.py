# Generated by Django 3.2.7 on 2021-10-28 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20211028_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='quantidade',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='total',
        ),
    ]
