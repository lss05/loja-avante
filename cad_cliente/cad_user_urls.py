from django.urls import path
from .views import caduserForm,novo_usuario

app_name = 'formcliente'

urlpatterns = [
    path('caduserForm',caduserForm,name='caduserForm'),
    path('creating_user/',novo_usuario,name='creating_user')
]