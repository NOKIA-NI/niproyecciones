from django.contrib import admin
from .models import Hwproyeccion
from import_export.admin import ImportExportModelAdmin
from .resources import HwActividadResource

@admin.register(Hwproyeccion)
class HwproyeccionAdmin(ImportExportModelAdmin):
    resource_class = HwActividadResource
    list_display = (
    'id',
    'siteName',
    'proyecto',
    'escenario',
    'banda',
    'agrupadores',
    'RFE',
    'parte',
    'estado',
    'cantidad_estimada',
    'lastUpdated',
    )
    list_filter = ('lastUpdated',)
    search_fields = ['id', 'siteName', 'parte']
