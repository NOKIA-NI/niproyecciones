from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget, ManyToManyWidget
from .models import FormatoEstacion, FormatoParte
from estaciones.models import Estacion
from partes.models import Parte

class FormatoEstacionResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'site_name'))

    class Meta:
        model = FormatoEstacion
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'estacion',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class FormatoParteResource(resources.ModelResource):
    formato_estacion = fields.Field(
        column_name='formato_estacion',
        attribute='formato_estacion',
        widget=ForeignKeyWidget(FormatoEstacion, 'estacion'))
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = FormatoParte
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'formato_estacion',
        'parte',
        'cantidad',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )