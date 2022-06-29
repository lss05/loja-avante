from django.shortcuts import render

# Create your views here.
def caduserForm(request):
    return render(request, 'cad_cliente/index.html')
