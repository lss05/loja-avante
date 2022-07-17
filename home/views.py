from django.shortcuts import render
from .models import GruposProdutos,Produtos

#minhas constantes
MY_APPS = ['home','autentication','cad_cliente','dashboardcliente',]
# Create your views here.

def Home(request,grupoprodutos=None):
    print(f'VALOR DE GET NA REQUISICAO: {request.GET}')

    logado = request.user.is_authenticated

    if logado:
        url_ = "area/area_cliente/"
    else:
        url_ = "cad_cliente/caduserForm"
        
    data = {'user_logado':int(logado),'desvio_url': url_}

    #Buscar grupos de produtos e ancoralos em views
    listagruposprodutos = GruposProdutos.objects.all()
    grupopadrao = listagruposprodutos[0] if not grupoprodutos else grupoprodutos

    # faco busca por todos os produtos da tela inicial ou caso seja solicitado.
    produtos_grupopadrao = Produtos.objects.filter(chavegrupo=grupopadrao)
    
    data.update({'gruposprodutos':listagruposprodutos,'produtos_grupopadrao':produtos_grupopadrao,'myapps': MY_APPS})

    print(f'verificando data {data}')
    
    return render(request, 'home/index.html',data)
