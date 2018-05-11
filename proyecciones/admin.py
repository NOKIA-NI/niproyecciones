from django.contrib import admin

from .models import Proyeccion, ProyeccionExtra
from import_export.admin import ImportExportModelAdmin
from .resources import ProyeccionResource, ProyeccionExtraResource

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
    'parte',
    'rfe',
    'estado_proyeccion',
    'cantidad_estimada',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion__site_name']

@admin.register(ProyeccionExtra)
class ProyeccionExtraAdmin(ImportExportModelAdmin):
    resource_class = ProyeccionExtraResource
    list_display = (
    'id',
    'estacion',
    'proyecto',
    'escenario',
    'banda',
    'agrupadores',
    'parte',
    'rfe',
    'estado_proyeccion',
    'cantidad_estimada',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion__site_name']
