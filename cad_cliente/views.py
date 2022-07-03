from django.shortcuts import render,redirect
from home.form_cliente import form_dados_cliente
from home.models import Clientes

# Create your views here.
cli = Clientes.objects.all()

def caduserForm(request):
    fields = ['Usuário','Senha','Nome','CPF','Email','Celular/Watsaap','Código Postal','Rua',
            'Número','Bairro','Cidade','Ponto de Referência']
    if request.method == "GET":
        #Esse trecho de código apenas renderiza o modelform na minha pagina html/ 
        # apenas envia os objetos para serem mostrados no html 
        forms = form_dados_cliente()   
        return render(request, 'cad_cliente/index.html',context={'forms': forms,'fields': fields})
    else:
        #Se o method for do tipo POST então está sendo recebido os dados do formulario para serem validados e
        # se for validados inserido no banco caso não for renderiza ou redireicona para a mesma padina que mando os 
        #dados.
        dados = request.POST
        print(dados)
        forms  =  form_dados_cliente(data=dados)
        if forms.is_valid():
            forms.save()
            forms = form_dados_cliente()
        else:
            print('Deu Erro - Form invalidado.')
        return render(request, 'cad_cliente/index.html',context={'forms': forms,'fields': fields})