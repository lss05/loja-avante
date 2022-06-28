from django.db import models
from datetime import datetime

# Create your models here.
class clientes(models.Model):
    #acesso a plataforma
    user_acesso = models.CharField(unique=True, max_length=45,blank=False, null=False)
    senha_acesso = models.CharField(max_length=45,blank=False, null=False)
    #dados pessoais
    id = models.AutoField(primary_key=True,auto_created=True)
    nome = models.CharField(max_length=45,blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=255,unique=True,null=False,blank=False)
    cel = models.CharField(max_length=14, null=True,blank=True)
    situacao_conta = models.BooleanField(default=True)
    #dados localização
    cep = models.CharField(max_length=9,null=False,blank=False)
    rua_ondemora = models.TextField(max_length=255,null=False,blank=False)
    num_casa = models.PositiveIntegerField(null=False,blank=False,default=0)
    bairro_ondemora = models.CharField(max_length=100)
    cidade = models.CharField(max_length=45,null=False,blank=False)
    estado = models.CharField(max_length=2,null=False,blank=False)
    ponto_referencia = models.TextField(max_length=255,null=True,blank=True)

    def __str__(self) -> str:
        return self.nome


class GruposProdutos(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    nome = models.CharField(max_length=45,blank=False, null=False)
    def __str__(self) -> str:
        return self.nome
class Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250,blank=False, null=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2,blank=False, null=False)
    descricao = models.TextField()
    qtde_estoque = models.PositiveIntegerField()
    chavegrupo = models.ForeignKey(GruposProdutos,on_delete=models.CASCADE)
    

class Promo_Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    chave_produto = models.ForeignKey(Produtos,on_delete=models.CASCADE)
    inicio_promo = models.DateTimeField(auto_now_add=True)
    fim_promo = models.DateTimeField(null=False,blank=False)
    taxadesconto = models.FloatField(blank=False,null=False)

#class formas de pagamento aceitos
class Formas_pagamentos(models.Model):
    forma_pagamento = models.CharField(max_length=40,unique=True,null=False,blank=False)
    def __str__(self) -> str:
        return self.forma_pagamento

class Transacoes(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    data_transacao = models.DateTimeField(auto_now_add=True)
    id_cliente = models.ForeignKey(clientes,on_delete=models.CASCADE)
    id_forma_pagamento = models.ForeignKey(Formas_pagamentos,on_delete=models.CASCADE)
    qtde_parcelamento = models.PositiveIntegerField(default=1)
    entrada_avista = models.FloatField(default=0.0)
    desconto = models.FloatField(default=0.0)
    #valor_frete = a combinar
