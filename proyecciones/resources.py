from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import Proyeccion

class ProyeccionResource(resources.ModelResource):

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
