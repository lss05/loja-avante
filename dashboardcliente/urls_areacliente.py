from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('area_cliente/',views.area_do_cliente,name='area_cliente')
]