from import_export import resources, fields
from import_export.widgets import (
    ForeignKeyWidget,
    DateWidget,
    DateTimeWidget,
    IntegerWidget,
    ManyToManyWidget,
    )
from .models import (
    Adicional,
    )
from estaciones.models import Estacion
from partes.models import Parte

class AdicionalResource(resources.ModelResource):
    # parte = fields.Field(
    #     column_name='parte',
    #     attribute='parte',
    #     widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = Adicional
        # exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'idadicionales_hw_sv',
        'wp',
        'siteName',
        'proyecto',
        'banda',
        'escenario',
        'tipo',
        'seccion',
        'parte',
        'cantidad',
        'proceso',
        'observaciones',
        'fecha_pedido',
        'usuario',
        'id',

        'recibido',
        'fecha_recibido',
        'responsable',
        'asignado',
        'fecha_asignado',
        'comentario',

        # 'estado',
        # 'subestado',
        # 'creado',
        # 'actualizado',
        )