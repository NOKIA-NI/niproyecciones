from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import Impacto
from estaciones.models import Estacion
from partes.models import Parte

class ImpactoResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'site_name'))
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = Impacto
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
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
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )
