from django.db import models
from django.contrib.auth.forms import PasswordChangeForm



# Create your models here.
#'user_acesso','senha_acesso','nome','cpf','email','cel','cep','rua_ondemora','num_casa','bairro_ondemora','cidade','ponto_referencia'

class Clientes(models.Model):
    #acesso a plataforma
    user_acesso = models.CharField(unique=True, max_length=45,blank=False, null=False,verbose_name='Usuário')
    senha_acesso = models.CharField(max_length=45,blank=False, null=False,verbose_name='Senha')
    #dados pessoais
    id = models.AutoField(primary_key=True,auto_created=True,verbose_name='ID')
    nome = models.CharField(max_length=45,blank=False, null=False,verbose_name='Nome')
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False,verbose_name='CPF')
    email = models.EmailField(max_length=255,unique=True,null=False,blank=False,verbose_name='Email')
    cel = models.CharField(max_length=11, null=True,blank=True,verbose_name='Celular/Watsaap')
    situacao_conta = models.BooleanField(default=True)
    #dados localização
    cep = models.CharField(max_length=8,null=False,blank=False,verbose_name='Código Postal')
    rua_ondemora = models.TextField(max_length=255,null=False,blank=False,verbose_name='Rua')
    num_casa = models.CharField(max_length=10,null=True,blank=True,verbose_name='Número')
    bairro_ondemora = models.CharField(max_length=100,verbose_name='Bairro')
    cidade = models.CharField(max_length=45,null=False,blank=False,verbose_name='Cidade')
    estado = models.CharField(max_length=2,null=False,blank=False,verbose_name='Estado')
    ponto_referencia = models.TextField(max_length=255,null=True,blank=True,verbose_name='Ponto de referência')

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
    valor = models.DecimalField(max_digits=6, decimal_places=2,blank=False, null=False)
    destaques = models.TextField(verbose_name='Destaques do produto.',blank=True,null=True)
    tag_descricao = models.TextField(max_length=250,verbose_name='Breve descrição do produto.',blank=True,null=True)
    ficha_tecnica = models.TextField(verbose_name='Ficha Técnica do produto.',blank=True,null=True)
    qtde_estoque = models.PositiveIntegerField()
    chavegrupo = models.ForeignKey(GruposProdutos,on_delete=models.CASCADE)
    img_foto = models.ImageField(upload_to='produtos',verbose_name='Imagem do Produto',max_length=250,default='foto-produto')


    def __str__(self):
        return self.name

class infoproduto_correios(models.Model):
    myproduto = models.OneToOneField(Produtos,on_delete=models.CASCADE,verbose_name='Chave do Produtos',primary_key=True)

    #Peso da encomenda, incluindo sua embalagem. O peso  deve  ser  informado  em  quilogramas.  Se  o formato for Envelope, o valor máximo permitido será 1 kg. 
    peso=models.DecimalField(verbose_name='Peso total da encomenda',default=0,null=False,blank=False,max_digits=3,decimal_places=1)

    formato = models.PositiveIntegerField(verbose_name='Tipo de encomenda',choices=((1,'Formato caixa/pacote'),(2,'Formato rolo/prisma'),(3,'Envelope')))

    #Comprimento da encomenda (incluindo embalagem), em centímetros.
    comprimento = models.DecimalField(verbose_name='Comprimento da encomenda',default=0,null=False,blank=False,max_digits=3,decimal_places=1)

    #Altura  da  encomenda  (incluindo  embalagem),  em centímetros. Se o formato for envelope, informar zero (0).
    altura = models.DecimalField(verbose_name='Altura da encomenda',default=0,null=False,blank=False,max_digits=3,decimal_places=1)

    #Largura da  encomenda  (incluindo embalagem), em centímetros.
    largura = models.DecimalField(verbose_name='Largura da encomenda',default=0,null=False,blank=False,max_digits=3,decimal_places=1)

    #Diâmetro da encomenda  (incluindo embalagem),  em centímetros. default é zero
    diametro = models.DecimalField(verbose_name='Diametro da encomenda',default=0,null=False,blank=False,max_digits=3,decimal_places=1)
    
    def __str__(self) -> str:
        return f'Informações de Frete para {self.myproduto}'

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
    id_cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    id_forma_pagamento = models.ForeignKey(Formas_pagamentos,on_delete=models.CASCADE)
    qtde_parcelamento = models.PositiveIntegerField(default=1)
    entrada_avista = models.FloatField(default=0.0)
    desconto = models.FloatField(default=0.0)
    #valor_frete = a combinar
    