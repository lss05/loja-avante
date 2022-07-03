from dataclasses import field
import email
from django import forms
from .models import Clientes

class form_dados_cliente(forms.ModelForm):
    user_acesso = forms.CharField(label='Usuário*', widget=forms.TextInput(attrs={"class":"useracesso",
    "type":"text","placeholder":"Digite seu usuário aqui..."},))
    senha_acesso = forms.CharField(label='Senha de Acesso*', widget=forms.TextInput(attrs={"class":"senhaacesso",
    "type":"password","placeholder":"Digite sua senha aqui..."},))
    nome = forms.CharField(label='Nome completo*', widget=forms.TextInput(attrs={"class":"nomecompleto",
    "type":"text","placeholder":"Informe seu nome completo"},))
    cpf = forms.CharField(label='CPF*', widget=forms.TextInput(attrs={"class":"mycpf",
    "type":"number","placeholder":"Informe seu CPF aqui, apenas números"},))
    email = forms.CharField(label='E-mail*', widget=forms.TextInput(attrs={"class":"myemail",
    "type":"email","placeholder":"Informe seu E-mail"},))
    cel = forms.CharField(label='Contato/Watsaap*', widget=forms.TextInput(attrs={"class":"contatowats",
    "type":"number","placeholder":"Informe um número de contato/watsaap"},))
    cep = forms.CharField(label='Código postal*', widget=forms.TextInput(attrs={"class":"codigopostal","id":"mycep",
    "type":"number","placeholder":"Informe seu Cep, apenas números","onkeypress": "return validarnumber(event,mycep,8)","maxlength":8},))
    class Meta:
        model = Clientes
        fields = ['user_acesso','senha_acesso','nome','cpf','email','cel','cep','rua_ondemora',
        'num_casa','bairro_ondemora','cidade','ponto_referencia']

        """
        def __ini__(self,*args,**kwargs):
            super(form_dados_cliente,self).__init__(*args,**kwargs)
            self.fields['senha_acesso'].label = 'Senha de acesso'
        """