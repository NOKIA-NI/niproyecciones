from django.contrib import admin
from .models import (
    HwProyeccion,
    HwEstacion,
    HwParte,
    HwSiteList,
    HwControlRfe,
    )
from import_export.admin import ImportExportModelAdmin
from .resources import (
    HwProyeccionResource,
    HwEstacionResource,
    HwParteResource,
    HwSiteListResource,
    HwControlRfeResource,
    )

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
    'ciudad',
    'scope_claro',
    'proyeccion_instalacion',
    'w_proyeccion_instalacion',
    'actividades',
    'bolsa',
    'w_fc_c',
    'status_nokia',
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
    search_fields = ['id', 'nombre_nokia']

@admin.register(HwSiteList)
class HwSiteListAdmin(ImportExportModelAdmin):
    resource_class = HwSiteListResource
    list_display = (
    'idsitesList',
    'siteName',
    'zona',
    'proyeccion_instalacion',
    'W_Proyeccion_Instalacion',
    'scope_claro',
    'Bolsa_HW',
    'w_fc_c',
    'status_nokia',
    'estado_HW',
    )
    # list_filter = ()
    search_fields = ['idsitesList', 'siteName']

@admin.register(HwControlRfe)
class HwControlRfeAdmin(ImportExportModelAdmin):
    resource_class = HwControlRfeResource
    list_display = (
    'id_hw_config',
    'wp',
    'siteName',
    'proyecto',
    'escenario',
    'banda',
    'seccion',
    'referencia',
    'cantidad',
    'parte',
    'total_smr',
    'fuente',
    'RFE',
    'so',
    'po',
    'bodega_origen',
    'bodega_origen_fecha',
    'issue_bodega_origen',
    'material_sobrante',
    'bts_status',
    'reemplazo',
    'po_date',
    'so_date',
    'envio_capex',
    'last_updated_ghw',
    'homologacion',
    )
    # list_filter = ()
    readonly_fields=[
        'wp',
        'siteName',
        'proyecto',
        'escenario',
        'banda',
        'seccion',
        'referencia',
        'cantidad',
        'parte',
        'total_smr',
        'fuente',
        'RFE',
        'bodega_origen_fecha',
        'bts_status',
        'reemplazo',
        'po_date',
        'so_date',
        'envio_capex',
        'last_updated_ghw',
    ]
    search_fields = ['id_hw_config', 'siteName', 'parte']
