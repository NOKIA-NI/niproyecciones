from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget, ManyToManyWidget
from .models import Estacion
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
        'scope_claro',
        'w_fc_imp',
        'w_fc_sal',
        'total_actividades',
        'estado_wr',
        'mos',
        'bolsa',
        'comunidades',
        'satelital',
        'impactar',
        'partes',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )
