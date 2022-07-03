from django.urls import path
from .views import caduserForm

app_name = 'formcliente'

urlpatterns = [
    path('caduserForm',caduserForm,name='caduserForm')
]