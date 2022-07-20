
from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.form_cliente import form_dados_cliente
from home.models import Clientes
from home.form_cliente import Form_User
from django.contrib.auth.models import User

# Create your views here.
cli = Clientes.objects.all()
ERROR_FIELD = 'Ops! dados inválidos - verifique os dados inseridos.'

def funcaoteste(widget=None):
    print(f'acessado de dentro do html {widget}')

def caduserForm(request):
    fields = ['Usuário','Senha','Nome','CPF','Email','Celular/Watsaap','Código Postal','Rua',
            'Número','Bairro','Cidade','Ponto de Referência']
    if request.method == "GET":
        #Esse trecho de código apenas renderiza o modelform na minha pagina html/ 
        # apenas envia os objetos para serem mostrados no html 
        forms = form_dados_cliente()   
        return render(request, 'cad_cliente/index.html',context={'forms': forms,'fields': fields,'funcaoteste':funcaoteste})
    else:
        #Se o method for do tipo POST então está sendo recebido os dados do formulario para serem validados e
        # se for validados inserido no banco caso não for renderiza ou redireicona para a mesma padina que mando os 
        #dados.
        dados = request.POST
        print(dados)
        forms  =  form_dados_cliente(data=dados)
        if forms.non_field_errors():
            print('Erro no form')
            
        if forms.is_valid():
            usuario = dados['user_acesso']
            senha = dados['senha_acesso']
            email = dados['email']
            
            newuser = User.objects.create_user(usuario,email,senha)
            newuser.save()
            forms.save()
            forms = form_dados_cliente()
            return redirect("/autentication/autenticar_/")
        else:
            print(f'Deu Erro - Form invalidado. {forms.non_field_errors()} OU {forms.errors}')
        return render(request, 'cad_cliente/index.html',context={'forms': forms,'fields': fields,'err':forms.errors})

def novo_usuario(request):
    data = request.POST
    f_user = Form_User(data=data)
    if request.method == 'GET':
        return render(request,'cad_cliente/cad_user.html',context={'form':Form_User})
    else:
        if f_user.is_valid():
            usuario = request.POST.get('username')
            senha = request.POST.get('password')
            email    = request.POST.get('email')
            print(f'minha senha: {senha}, {usuario}, {email}')
            user = User.objects.filter(username=usuario)
            print(f'verificando se tem algun usuario cadastrado: {user}')
            if not user:
                newuser = User.objects.create_user(usuario,email,senha)
                newuser.save()
                f_user = Form_User()
                return HttpResponse('Usuário criando com sucesso!')
        return render(request,'cad_cliente/cad_user.html',context={'form':f_user})

