from django.urls import path
from .views import caduserForm

app_name = 'formcliente'

print('PASSOU NO CAD_USER_URL NA LINHA 7')

urlpatterns = [
    path('caduserForm',caduserForm,name='caduserForm')
]