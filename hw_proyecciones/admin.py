from django.contrib import admin
from .models import (
    HwProyeccion,
    HwEstacion,
    HwParte,
    HwSiteList,
    HwControlRfe,
    DrillDown,
    )
from import_export.admin import ImportExportModelAdmin
from .resources import (
    HwProyeccionResource,
    HwEstacionResource,
    HwParteResource,
    HwSiteListResource,
    HwControlRfeResource,
    DrillDownResource,
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
    'fecha_solicitud_hw',
    'solicitante_asignacion_hw',
    'solicitud_hw',
    'PO_Status',
    'Antena_Issue',
    'Status_Despachos',
    'gap_rfe_sitio',
    'Cosite',
    )
    list_filter = ('Bolsa_HW', 'status_nokia', 'solicitud_hw')
    search_fields = ['idsitesList', 'siteName']

@admin.register(DrillDown)
class DrillDownAdmin(ImportExportModelAdmin):
    resource_class = DrillDownResource
    list_display = (
    'id_drill_down_d1',
    'Site_Name',
    'Implemented',
    'TSS',
    'RFIC',
    'FC_RFIC',
    'CPO_Status1',
    'CPO_Status2',
    'HW_Status',
    'FC_HW',
    'Status_Despachos',
    'FC_Antenas',
    )
    # list_filter = ()
    # readonly_fields = [
    # 'Site_Name',
    # 'Implemented',
    # 'TSS',
    # 'RFIC',
    # 'FC_RFIC',
    # 'CPO_Status1',
    # 'CPO_Status2',
    # 'HW_Status',
    # 'FC_HW',
    # 'Status_Despachos',
    # 'FC_Antenas',
    # ]
    search_fields = ['id_drill_down_d1', 'Site_Name']
