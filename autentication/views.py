from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.forms import Field
from django.http import HttpResponseRedirect

# Create your views here.

def autenticar(request):
    Labelerror = Field(label='Erro! Usuário ou Senha incorreto')
    labelerror = 'Erro! Usuário ou Senha incorreto'
    data = {'error':labelerror,'labelerror':Labelerror}
    #print(f'Verificando field label: {Labelerror}')

    # se o cliente não estiver logado e a requisição for para logar entra no if para renderizar a pagina de login
    if request.method == 'GET' and not request.user.is_authenticated:
        data['error']=''
        return render(request, 'autentication/tela-login.html',data)
    # se o cliente não esitver logado e a requisição for para logar e for do tipo POST entra aqui para validar o cliente.
    elif request.method == 'POST' and not request.user.is_authenticated:
        #altentico usuário caso ele exista
        usuario = request.POST.get('username')
        senha = request.POST.get('password')

        #1º Busco usuario que deseja logar
        user = authenticate(username=usuario,password=senha)
        print(f'verificando se o usuario foi altenticado com sucesso: {user}')
        
        #2º Se o usuario não for none pode ser logado.
        if not user:
            return  render(request, 'autentication/tela-login.html',data)
        else:
            login(request,user)
            url = '/?grupo=promocoes&login=True'
            #return redirect(f'home:Home')
            return HttpResponseRedirect(url)
    #desloga o cliente e redireciona para HOME
    else:
        logout(request)
        url = '/?grupo=promocoes&logout=False'
        return redirect(url)
    
    