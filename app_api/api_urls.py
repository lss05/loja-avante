from django.urls import path
from . import views

app_name = 'appapi'

urlpatterns = [
    path('acesso_api/',views.my_apis,name='acesso_api'),
    path('acesso_api_end/',views.my_apis_responseJSON,name='acesso_api_end'),
    path('acesso_api_end2/<int:cep>/',views.my_apis_responseJSON2,name='acesso_api_end2'),
    path('p_produtos_forgrupo/<str:grupo>/<int:id>/', views.p_myapi_produtos_to_grupo,name='req_produtos1'),
    path('i_produtos_forgrupo/<str:grupo>/<int:iid>/', views.i_myapi_produtos_to_grupo,name='req_produtos'),

]