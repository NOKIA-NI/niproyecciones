from django.contrib import admin

from .models import (
FormatoEstacion,
FormatoParte,
FormatoClaro,
FormatoClaroTotal,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
FormatoEstacionResource,
FormatoParteResource,
FormatoClaroResource,
FormatoClaroTotalResource,
)

@admin.register(FormatoEstacion)
class FormatoEstacionAdmin(ImportExportModelAdmin):
    resource_class = FormatoEstacionResource
    list_display = (
    'id',
    'estacion',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion__site_name']

@admin.register(FormatoParte)
class FormatoParteAdmin(ImportExportModelAdmin):
    resource_class = FormatoParteResource
    list_display = (
    'id',
    'formato_estacion',
    'parte',
    'cantidad',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'formato_estacion__estacion__site_name', 'parte__parte_nokia']

@admin.register(FormatoClaro)
class FormatoClaroAdmin(ImportExportModelAdmin):
    resource_class = FormatoClaroResource
    list_display = (
    'id',
    'id_sitio',
    'sitio',
    'proyecto',
    'sap',
    'descripcion',
    'qty',
    'ciudad',
    'regional',
    'semana',
    'mes',
    'generado',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'sitio__site_name']

@admin.register(FormatoClaroTotal)
class FormatoClaroTotalAdmin(ImportExportModelAdmin):
    resource_class = FormatoClaroTotalResource
    list_display = (
    'id',
    'parte',
    'cod_sap',
    'capex',
    'grupo_parte',
    'total',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'parte__parte_nokia']
