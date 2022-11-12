"""PJI3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pji3g54app.views import (home, index, form, formpf, create, view, edit, update, delete, create_user,
                              store_user, vmoleo, painel, dologin, dologout, dashboard)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('form/', form, name='form'),
    path('formpf/', formpf, name='formpf'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('create_user/', create_user, name='create_user'),
    path('store_user/', store_user, name='store_user'),
    path('vmoleo/<str:inputCEP>', vmoleo, name='vmoleo'),
    path('painel/', painel, name='painel'),
    path('dologin/', dologin, name='dologin'),
    path('dologout/', dologout, name='dologout'),
    path('dashboard/', dashboard, name='dashboard'),
]
