from django.shortcuts import render

# Create your views here.
def autenticar(request):
    return render(request, 'autentication/site_login.html')

def cad_user(request):
    return render(request, 'autentication/cadastrar_user.html')

def nova_senha(request):
    return render(request, 'autentication/recupera_senha.html')

def info_contatos(request):
    return render(request, 'autentication/contatos.html')