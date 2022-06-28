from django.urls import path,include
from .views import *
app_name = 'home'

urlpatterns = [
    path('',Home,name='Home'),
    path('app_login/',include('autentication.autentication_urls',namespace='autentication'))
]