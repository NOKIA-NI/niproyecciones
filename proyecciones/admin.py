from django.contrib import admin

from .models import Proyeccion
from import_export.admin import ImportExportModelAdmin
from .resources import ProyeccionResource

#@admin.register(Proyeccion)
#class ProyeccionAdmin(admin.ModelAdmin):
#    pass

@admin.register(Proyeccion)
class ProyeccionAdmin(ImportExportModelAdmin):
    resource_class = ProyeccionResource
    list_display = (
    'id',
    'estacion',
    'proyecto',
    'escenario',
    'banda',
    'agrupadores',
    'rfe',
    'parte',
    'estado_proyeccion',
    'cantidad_estimada',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion', 'parte']
