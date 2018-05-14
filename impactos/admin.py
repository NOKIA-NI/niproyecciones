from django.contrib import admin

from .models import Impacto
from import_export.admin import ImportExportModelAdmin
from .resources import ImpactoResource

#@admin.register(Impacto)
#class ImpactoAdmin(admin.ModelAdmin):
#    pass

@admin.register(Impacto)
class ImpactoAdmin(ImportExportModelAdmin):
    resource_class = ImpactoResource
    list_display = (
    'id',
    'estacion',
    'w_fc_sal',
    'w_fc_imp',
    'bolsa',
    'parte',
    'grupo_parte',
    'cantidad_estimada',
    'tipo_impacto',
    'impactado',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado', 'impactado')
    search_fields = ['id', 'estacion__site_name']
