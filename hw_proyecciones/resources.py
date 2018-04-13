from import_export import resources
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import Hwproyeccion

class HwActividadResource(resources.ModelResource):

    class Meta:
        model = Hwproyeccion
        # exclude = ('id',)
        export_order = (
        'id',
        'siteName',
        'proyecto',
        'escenario',
        'banda',
        'agrupadores',
        'RFE',
        'parte',
        'estado',
        'cantidad_estimada',
        'lastUpdated',
        )
