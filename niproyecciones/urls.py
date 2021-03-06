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
admin.site.site_header = 'NI Hardware'
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('tareas/', include('tareas.urls', namespace='tareas')),
    path('consultas/', include('consultas.urls', namespace='consultas')),
    path('estaciones/', include('estaciones.urls', namespace='estaciones')),
    path('partes/', include('partes.urls', namespace='partes')),
    path('hw_proyecciones/', include('hw_proyecciones.urls', namespace='hw_proyecciones')),
    path('proyecciones/', include('proyecciones.urls', namespace='proyecciones')),
    path('hw_actividades/', include('hw_actividades.urls', namespace='hw_actividades')),
    path('consumos/', include('consumos.urls', namespace='consumos')),
    path('llegadas/', include('llegadas.urls', namespace='llegadas')),
    path('existencias/', include('existencias.urls', namespace='existencias')),
    path('resultados/', include('resultados.urls', namespace='resultados')),
    path('impactos/', include('impactos.urls', namespace='impactos')),
    path('formatos/', include('formatos.urls', namespace='formatos')),
    path('rastreos/', include('rastreos.urls', namespace='rastreos')),
    path('asignaciones/', include('asignaciones.urls', namespace='asignaciones')),
    path('adicionales/', include('adicionales.urls', namespace='adicionales')),

    # third
    path('advanced_filters/', include('advanced_filters.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
