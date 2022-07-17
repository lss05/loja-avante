from django.shortcuts import redirect, render
from django.http import JsonResponse,HttpResponse
from home import views
import json

from home.models import GruposProdutos

# Create your views here.
def my_apis(request):
    return render(request,'app_api/cep.html')
def my_apis_responseJSON(request):
    end = {
        'cep':65930000,
        'cidade': 'açailandia',
        'estado': 'MA'
    }
    return JsonResponse(end)
def my_apis_responseJSON2(request,cep):
    print(cep)
    end = {
        'cep':f'{cep}',
        'cidade': 'açailandia',
        'estado': 'MA'
    }
    return HttpResponse(json.dumps(end))
def p_myapi_produtos_to_grupo(request,grupo,id): #p na frente da funcao indica que é uma api publica 
    print(f'Meu grupo é: {grupo} e o id: {id} e o meu app é')
    produtos = views.Produtos.objects.filter(chavegrupo=views.GruposProdutos.objects.filter(nome=grupo)[0].id)
    return JsonResponse({'produto_1':'Active 20 ultra'})






def i_myapi_produtos_to_grupo(request,grupo,id): # o i na frente da função que dizer que é interno e server para renderizar template.
    print(f'Meu grupo é: {grupo} e o id: {id} e o meu app é')
    produtos = views.Produtos.objects.filter(chavegrupo=views.GruposProdutos.objects.filter(nome=grupo)[0].id)
    
    return render(request,'',produtos)

