from django.urls import path
from . import views

app_name = 'autentication'

urlpatterns = [
    path('autenticar_/',views.autenticar,name='autenticar')
]