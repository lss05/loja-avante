from django.shortcuts import render


# Create your views here.

def Home(request):
    print(f'Pagina Home - verificando quem está logado: {request.user.is_authenticated}')
    logado = request.user.is_authenticated
    data = {'user_logado':int(logado)}
    if logado:
        ancora_areacliente = "{% url 'dashboard:area_cliente' %}"
        data['ancora_areacliente'] = ancora_areacliente
        data['verbosename_areacliente'] = 'Área do cliente'
    return render(request, 'home/index.html',data)
