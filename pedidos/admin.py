from django.contrib import admin
from .models import Categoria, Prato, Pedido, Estoque, ItemPedido, Caixa

admin.site.register(Categoria)
admin.site.register(Prato)
admin.site.register(Pedido)
admin.site.register(Estoque)
admin.site.register(ItemPedido)
admin.site.register(Caixa)