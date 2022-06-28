from django.urls import path
from . import views

app_name = 'autentication'

urlpatterns = [
    #path('autentication/',autenticar,name='autentication'),
    path('autenticar/',views.autenticar,name='autenticar'),
    path('cad_user/',views.cad_user,name='cad_user'),
    path('info_contatos/',views.info_contatos,name='info_contatos'),
    path('nova_senha/',views.nova_senha,name='nova_senha'),
]