from django.shortcuts import render
from home.form_cliente import form_dados_cliente
from home.models import Clientes

# Create your views here.
cli = Clientes.objects.all()

def caduserForm(request):
    forms = form_dados_cliente()   
    fields = ['Usuário','Senha','Nome','CPF','Email','Celular/Watsaap','Código Postal','Rua',
        'Número','Bairro','Cidade','Ponto de Referência']
    
    """
    print(f'objeto form aqui: {type(form)}')
    context = {
        'form' : form,
        'clientes': cli[0]
    }"""
    return render(request, 'cad_cliente/index.html',context={'forms': forms,'fields': fields})
