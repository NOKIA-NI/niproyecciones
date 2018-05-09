from django.contrib import admin

from .models import Parte
from import_export.admin import ImportExportModelAdmin
from .resources import ParteResource

#@admin.register(Parte)
#class ParteAdmin(admin.ModelAdmin):
#    pass

@admin.register(Parte)
class ParteAdmin(ImportExportModelAdmin):
    resource_class = ParteResource
    list_display = (
    'id',
    'cod_sap',
    'parte_nokia',
    'capex',
    'grupo_parte',
    'impactar',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'cod_sap', 'parte_nokia']
