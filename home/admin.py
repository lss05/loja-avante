from django.contrib import admin
from .models import GruposProdutos,Produtos,Promo_Produtos
from .models import Clientes,Formas_pagamentos,Transacoes
from .models import infoproduto_correios
# Register your models here.

admin.site.register([GruposProdutos,Produtos,Promo_Produtos,infoproduto_correios])
admin.site.register([Clientes,Formas_pagamentos,Transacoes])

