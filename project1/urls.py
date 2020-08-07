"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from project1.views import helloWorld, getData, calculaEdad, helloWorldVar, helloWorldVar2, helloWorldVar3, helloWorldVar4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloWorld/', helloWorld),
    path('helloWorldVar/', helloWorldVar),
    path('helloWorldVar2/', helloWorldVar2),
    path('helloWorldVar3/', helloWorldVar3),
    path('helloWorldVar4/', helloWorldVar4),
    path('getdata/', getData),
    path('edad/<int:edad>/<int:anyo>', calculaEdad)
]
