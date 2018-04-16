from import_export import resources
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import HwProyeccion

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
