# Generated by Django 3.2.7 on 2021-11-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_caixa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='pagamento',
            field=models.IntegerField(choices=[(1, 'DINHEIRO'), (2, 'CARTÃO DÉBITO'), (3, 'CARTÃO CRÉDITO'), (4, 'PIX')]),
        ),
        migrations.AlterField(
            model_name='caixa',
            name='status',
            field=models.IntegerField(choices=[(1, 'EM ANDAMENTO'), (2, 'PAGO'), (3, 'PRONTO')]),
        ),
    ]
