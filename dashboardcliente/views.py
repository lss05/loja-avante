from django.shortcuts import render

# Create your views here.
def area_do_cliente(request):
    modelocliente = {} #envio o FormModel ou informações do cliente.
    return render(request,'dashboardcliente/dashboard.html')