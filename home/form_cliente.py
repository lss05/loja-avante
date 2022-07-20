from django import forms
from .models import Clientes
from django.contrib.auth.models import User

class Form_User(forms.ModelForm):
    username = forms.CharField(label='Usuário*', widget=forms.TextInput(attrs={"class":"useracesso input-text",
    "type":"text","placeholder":"Digite seu usuário aqui...","name":"username","maxlength":150,"required":"","id":"id_username"}))

    password = forms.CharField(label='Senha*', widget=forms.TextInput(attrs={"class":"senhaacesso input-text",
    "type":"password","placeholder":"Digite sua senha aqui..."}))

    email = forms.CharField(label='E-mail*', widget=forms.TextInput(attrs={"class":"my_email input-text",
    "type":"email","placeholder":"Digite seu E-mail","name":"email", "maxlength":254,"id":"id_email"}))

    #<input type="email" name="email" maxlength="254" id="id_email">

    class Meta:
        model = User
        fields = ["username","password","email"]

class form_dados_cliente(forms.ModelForm):
    user_acesso = forms.CharField(label='Usuário*', widget=forms.TextInput(attrs={"class":"useracesso input-text",
    "type":"text","placeholder":"Digite seu usuário aqui..."},))
    senha_acesso = forms.CharField(label='Senha de Acesso*', widget=forms.TextInput(attrs={"class":"senhaacesso input-text",
    "type":"password","placeholder":"Digite sua senha aqui..."},))
    nome = forms.CharField(label='Nome completo*', widget=forms.TextInput(attrs={"class":"nomecompleto input-text",
    "type":"text","placeholder":"Informe seu nome completo"},))
    cpf = forms.CharField(label='CPF*', widget=forms.TextInput(attrs={"class":"mycpf input-text","id":"mycpf",
    "type":"number","min":0,"placeholder":"Informe seu CPF aqui, apenas números","onkeypress": "return validarnumber(event,mycpf,11)"},))
    email = forms.CharField(label='E-mail*', widget=forms.TextInput(attrs={"class":"myemail input-text",
    "type":"email","placeholder":"Informe seu E-mail"},))
    cel = forms.CharField(label='Contato/Watsaap*', widget=forms.TextInput(attrs={"class":"contatowats input-text","onkeypress": "return validarnumber(event,mycel,16)",
    "type":"number","min":0,"placeholder":"Informe um número de contato/watsaap","id":"mycel"},))

    cep = forms.CharField(label='Código postal*', widget=forms.TextInput(attrs={"class":"codigopostal input-text","id":"mycep",
    "type":"number","min":0,"placeholder":"Informe seu Cep, apenas números","onkeypress": "return validarnumber(event,mycep,8)","maxlength":8},))

    num_casa = forms.CharField(label='Número*', widget=forms.TextInput(attrs={"class":"numcasa input-text","id":"mynumero",
    "type":"text","min":0,"placeholder":"Informe número de sua residência"},))
    bairro_ondemora = forms.CharField(label='Bairro*', widget=forms.TextInput(attrs={"class":"bairro input-text","id":"mybairro",
    "type":"text","placeholder":"Informe seu bairro"},))
    cidade = forms.CharField(label='Cidade*', widget=forms.TextInput(attrs={"class":"cidade input-text","id":"mycidade",
    "type":"text","min":0,"placeholder":"Informe sua cidade"},))
    estado = forms.CharField(max_length=2, label='Estado*', widget=forms.TextInput(attrs={"class":"estado input-text","id":"myestado",
    "type":"text","max_length":2,"placeholder":"Informe seu estado"},))

    """
    ponto_referencia = forms.Textarea(label='Ponto de referêcia*', widget=forms.TextInput(attrs={"class":"referencia input-text","id":"myreferencia",
    "type":"text","min":0,"placeholder":"Informe um ponto de referência"},))""" 
    class Meta:
        model = Clientes
        fields = ['user_acesso','senha_acesso','nome','cpf','email','cel','cep','rua_ondemora',
        'num_casa','bairro_ondemora','cidade','estado','ponto_referencia']

        """
        def __ini__(self,*args,**kwargs):
            super(form_dados_cliente,self).__init__(*args,**kwargs)
            self.fields['senha_acesso'].label = 'Senha de acesso'
        """