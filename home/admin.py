from django.contrib import admin
from .models import GruposProdutos,Produtos,Promo_Produtos
from .models import Clientes,Formas_pagamentos,Transacoes
# Register your models here.

admin.site.register([GruposProdutos,Produtos,Promo_Produtos])
admin.site.register([Clientes,Formas_pagamentos,Transacoes])

