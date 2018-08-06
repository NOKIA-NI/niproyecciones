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
    PoZina,
    SitioBolsa,
    SitioBulk,
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
        'comentario_bodega',
        'so',
        'po',
        'familia',
        'caracteristicas',
        'puertos',

        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class EstadoPoResource(resources.ModelResource):

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

class PoZinaResource(resources.ModelResource):

    class Meta:
        model = PoZina
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'cpo_number',
        'so_jumper',
        'so_bts',
        'project',
        'site_name',
        'material_description',
        'parte_capex',
        'quantity',

        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class SitioBolsaResource(resources.ModelResource):

    class Meta:
        model = SitioBolsa
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'estacion',

        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class SitioBulkResource(resources.ModelResource):

    class Meta:
        model = SitioBulk
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'estacion',

        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )