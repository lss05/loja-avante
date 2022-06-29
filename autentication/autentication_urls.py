from django.urls import path
from . import views

app_name = 'autentication'

urlpatterns = [
    #path('autentication/',autenticar,name='autentication'),
    path('autenticar_/',views.autenticar,name='autenticar')
]