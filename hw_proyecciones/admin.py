from django.contrib import admin
from .models import HwProyeccion, HwEstacion, HwParte
from import_export.admin import ImportExportModelAdmin
from .resources import HwProyeccionResource, HwEstacionResource, HwParteResource

@admin.register(HwProyeccion)
class HwProyeccionAdmin(ImportExportModelAdmin):
    resource_class = HwProyeccionResource
    list_display = (
    'id',
    'siteName',
    'proyecto',
    'escenario',
    'banda',
    'agrupadores',
    'rfe',
    'parte',
    'estado',
    'cantidad_estimada',
    'lastUpdated',
    'created',
    )
    list_filter = ('lastUpdated', 'created', 'estado')
    search_fields = ['id', 'siteName', 'parte']

@admin.register(HwEstacion)
class HwEstacionAdmin(ImportExportModelAdmin):
    resource_class = HwEstacionResource
    list_display = (
    'id',
    'siteName',
    'region',
    'scope_claro',
    'proyeccion_instalacion',
    'w_proyeccion_instalacion',
    'actividades',
    'bolsa',
    'scope_c',
    )
    # list_filter = ()
    search_fields = ['id', 'siteName']

@admin.register(HwParte)
class HwParteAdmin(ImportExportModelAdmin):
    resource_class = HwParteResource
    list_display = (
    'id',
    'cod_capex',
    'nombre_nokia',
    'nombre_capex',
    'seccion_parte',
    )
    # list_filter = ()
    search_fields = ['id']
