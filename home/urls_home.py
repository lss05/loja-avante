from django.urls import path
from .views import *


app_name = 'home'

urlpatterns = [
    path('',Home,name='Home'),
    path('edit_senha/',view_alterarsenha,name='newsenha')
]