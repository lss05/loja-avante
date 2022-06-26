from django.urls import path
from .views import autenticar

app_name = 'autentication'

urlpatterns = [
    path('autentication/',autenticar,name='autentication'),
]