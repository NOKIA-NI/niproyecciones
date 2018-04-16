from django.contrib import admin
from .models import HwProyeccion
from import_export.admin import ImportExportModelAdmin
from .resources import HwProyeccionResource

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
