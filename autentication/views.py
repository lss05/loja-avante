from django.shortcuts import render,redirect

# Create your views here.
def autenticar(request):
    if request.method == 'POST':
        print('VALIDANDO FORM USUARIO')
        print(request.POST)

        return redirect('/')
    
    return render(request, 'autentication/tela-login.html')