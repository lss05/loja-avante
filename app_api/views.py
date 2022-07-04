from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json

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