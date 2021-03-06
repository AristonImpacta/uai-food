# Generated by Django 3.2.7 on 2021-11-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20211117_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='caixa',
            name='pagamento',
            field=models.IntegerField(choices=[(1, 'DINHEIRO'), (2, 'CARTÃO DÉBITO'), (3, 'CARTÃO CRÉDITO'), (4, 'PIX')], default=0),
        ),
        migrations.AddField(
            model_name='caixa',
            name='status',
            field=models.IntegerField(choices=[(1, 'EM ANDAMENTO'), (2, 'PAGO'), (3, 'PRONTO')], default=0),
        ),
    ]
