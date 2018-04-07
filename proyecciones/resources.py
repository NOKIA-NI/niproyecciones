from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import Proyeccion
from estaciones.models import Estacion
from partes.models import Parte

class ProyeccionResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'site_name'))
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = Proyeccion
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'estacion',
        'proyecto',
        'escenario',
        'banda',
        'agrupadores',
        'rfe',
        'parte',
        'estado_proyeccion',
        'cantidad_estimada',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )
