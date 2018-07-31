from import_export import resources, fields
from import_export.widgets import (
    ForeignKeyWidget,
    DateWidget,
    DateTimeWidget,
    IntegerWidget,
    ManyToManyWidget,
    )
from .models import (
    AsignacionBulk,
    AsignacionAntena,
    EstadoPo,
    )
from estaciones.models import Estacion
from partes.models import Parte

class AsignacionBulkResource(resources.ModelResource):
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = AsignacionBulk
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'parte',
        'cod_sap',
        'capex',
        'cantidad',
        'cod_bodega',
        'bodega',
        'comentario_bodega',
        'so',
        'po',

        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class AsignacionAntenaResource(resources.ModelResource):
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = AsignacionAntena
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'parte',
        'cod_sap',
        'capex',
        'cantidad',
        'cod_bodega',
        'bodega',
        'familia',
        'caracteristicas',
        'puertos',

        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class EstadoPoResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'estacion'))

    class Meta:
        model = EstadoPo
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'numero_po',
        'estacion',
        'project',
        'bts',
        'bts_status',
        'bts_arrival_week',
        'jumper',
        'jumper_status',
        'jumper_arrival_week',
        'fxcb_bts',
        'fxcb_status',
        'customs_ceared',
        'sr',
        'awb',
        'eta',
        'delivery',
        'pre_pgi',
        'fc_impl',
        'fxcb_qty',
        'annotation',
        'comprometido',
        'share',
        'w_reviewed',
        'columna_924',

        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )