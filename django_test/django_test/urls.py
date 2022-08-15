"""django_test URL Configuration

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

from django_test.views import saludo, canelones, dia_de_hoy, saludo_con_nombre, año_de_nacimiento, plantilla
from relations.views import test


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='view_de_saludo'),
    path('canelones/', canelones, name='canelones'),
    path('dia-de-hoy/', dia_de_hoy, name='dia_de_hoy'),
    path('saludo-con-nombre/<str:nombre>/', saludo_con_nombre, name='saludo_con_nombre'),
    path('nacimiento/<int:edad>/', año_de_nacimiento, name='nacimiento'),
    path('plantilla/', plantilla, name='plantilla'),
    path('test/', test, name='test')
]
