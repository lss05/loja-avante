"""myprojeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('home.urls_home',namespace='home')),
    
    path('autentication/',include('autentication.autentication_urls',namespace='autentication')),
    path('cad_cliente/',include('cad_cliente.cad_user_urls',namespace='formcliente')),
    path('response_api/',include('app_api.api_urls',namespace='appapi')),
    path('accounts/', include('django.contrib.auth.urls')), #Add Django site authentication urls (for login, logout, password management)
    path('admin/', admin.site.urls),
    path('area/',include('dashboardcliente.urls_areacliente',namespace='dashboard'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
