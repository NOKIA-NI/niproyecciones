from django.contrib import admin

from .models import HwActividad
from import_export.admin import ImportExportModelAdmin
from .resources import HwActividadResource

#@admin.register(HwActividad)
#class HwActividadAdmin(admin.ModelAdmin):
#    pass

@admin.register(HwActividad)
class HwActividadAdmin(ImportExportModelAdmin):
    resource_class = HwActividadResource
    list_display = (
    'id',
    'estacion',
    'proyeccion',
    'proyeccion_extra',
    'parte',
    'lsm',
    'calculo_hw',
    'impactar',
    'cambiar_impactar',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion__site_name','proyeccion__id', 'proyeccion_extra__id', 'parte__parte_nokia' ]
