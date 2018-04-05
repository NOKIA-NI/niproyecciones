"""niproyecciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
admin.site.site_header = 'NI Proyecciones'
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('estaciones/', include('estaciones.urls', namespace='estaciones')),
    path('partes/', include('partes.urls', namespace='partes')),
    path('proyecciones/', include('proyecciones.urls', namespace='proyecciones')),
    path('hw_actividades/', include('hw_actividades.urls', namespace='hw_actividades')),
    path('consumos/', include('consumos.urls', namespace='consumos')),
]
