from django.contrib import admin

from .models import Estacion
from import_export.admin import ImportExportModelAdmin
from .resources import EstacionResource

#@admin.register(Estacion)
#class EstacionAdmin(admin.ModelAdmin):
#    pass

@admin.register(Estacion)
class EstacionAdmin(ImportExportModelAdmin):
    resource_class = EstacionResource
    list_display = (
    'id',
    'site_name',
    'region',
    'scope_claro',
    'w_fc_imp',
    'total_actividades',
    'estado_wr',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'site_name']
