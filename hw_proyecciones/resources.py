from import_export import resources
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import (
    HwProyeccion,
    HwEstacion,
    HwParte,
    HwSiteList,
    HwControlRfe,
)

class HwProyeccionResource(resources.ModelResource):

    class Meta:
        model = HwProyeccion
        # exclude = ('id',)
        export_order = (
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

class HwEstacionResource(resources.ModelResource):

    class Meta:
        model = HwEstacion
        # exclude = ('id',)
        export_order = (
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

class HwParteResource(resources.ModelResource):

    class Meta:
        model = HwParte
        # exclude = ('id',)
        export_order = (
        'id',
        'cod_capex',
        'nombre_nokia',
        'nombre_capex',
        'seccion_parte',
        )

class HwSiteListResource(resources.ModelResource):

    class Meta:
        model = HwSiteList
        # exclude = ('id',)
        export_order = (
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
        )

class HwControlRfeResource(resources.ModelResource):

    class Meta:
        model = HwControlRfe
        # exclude = ('id',)
        import_id_fields = ('id_hw_config',)
        export_order = (
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
