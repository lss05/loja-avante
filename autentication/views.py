from django.shortcuts import render

# Create your views here.
def autenticar(request):
    return render(request, 'autentication/site_login.html')