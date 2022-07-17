from urllib.request import ProxyDigestAuthHandler
from django.shortcuts import render
from .models import GruposProdutos,Produtos,Promo_Produtos

#minhas constantes
MY_APPS = ['home','autentication','cad_cliente','dashboardcliente',]
# Create your views here.

def Home(request):
    grupoprodutos = list(request.session.values())
    print(f'VALOR DE GET NA REQUISICAO: {grupoprodutos}')

    
    logado = request.user.is_authenticated

    if logado:
        url_ = "area/area_cliente/"
    else:
        url_ = "cad_cliente/caduserForm"
        
    data = {'user_logado':int(logado),'desvio_url': url_}

    #Buscar grupos de produtos e ancoralos em views
    listagruposprodutos = GruposProdutos.objects.all()

    #pegando apenas o nome do grupo seja o padrão que pode ser o grupo que está na promoção ou algum outro que o usuario tenha clickado na views
    try:
        grupo = request.session['grupo']
        produtos_padrao = Produtos.objects.filter(chavegrupo=GruposProdutos.objects.filter(nome=grupo)[0].id)
        print(f'VERIFICANDO VALOR DOS PRODUTOS DO GRUPO ESCOLHIDO PELO USUARIO: {produtos_padrao}')
    except KeyError:
        #quando o acesso for o 1 será apresentado os produtos que estão não promoção
        grupo = listagruposprodutos[0].nome
        produtos_padrao = Promo_Produtos.objects.all()
        produtos_padrao.values_list()
        print(f'VERIFICANDO VALOR DOS PRODUTOS DA PROMOÇÃO: {produtos_padrao}')

    # faco busca por todos os produtos da tela inicial ou caso seja solicitado.
    produtos_padrao = Produtos.objects.filter(chavegrupo=GruposProdutos.objects.filter(nome=grupo)[0].id)
    
    data.update({'gruposprodutos':listagruposprodutos,'produtos_grupopadrao':produtos_padrao,'myapps': MY_APPS,'sessios':request.session})
    
    return render(request, 'home/index.html',data)
