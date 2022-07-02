from dataclasses import field
from django import forms
from .models import Clientes

class form_dados_cliente(forms.ModelForm):
    senha_acesso = forms.CharField(label='Senha de Acesso(*)', widget=forms.TextInput(attrs={"class":"senhaacesso",
    "type":"password","placeholder":"Digite sua senha aqui..."},))

    def __ini__(self,*args,**kwargs):
        super(form_dados_cliente,self).__init__(*args,**kwargs)
        self.fields['senha_acesso'].label = 'Senha de acesso'
    class Meta:
        model = Clientes
        fields = ['user_acesso','senha_acesso','nome','cpf','email','cel','cep','rua_ondemora',
        'num_casa','bairro_ondemora','cidade','ponto_referencia']