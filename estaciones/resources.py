from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget, ManyToManyWidget
from .models import Estacion, BitacoraEstacion
from partes.models import Parte

class EstacionResource(resources.ModelResource):
    partes = fields.Field(
        column_name='partes',
        attribute='partes',
        widget=ManyToManyWidget(Parte, separator=',', field='parte_nokia'))

    class Meta:
        model = Estacion
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'site_name',
        'region',
        'ciudad',
        'scope_claro',
        'w_fc_sal',
        'w_fc_imp',
        'w_fc_c',
        'total_actividades',
        'estado_wr',
        'mos',
        'bolsa',
        'status_nokia',
        'comunidades',
        'satelital',
        'impactar',
        'partes',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class BitacoraEstacionResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'site_name'))

    class Meta:
        model = BitacoraEstacion
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'estacion',
        'fecha_bitacora',
        'observaciones',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )
