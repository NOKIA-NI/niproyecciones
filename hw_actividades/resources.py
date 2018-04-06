from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import HwActividad

class HwActividadResource(resources.ModelResource):

    class Meta:
        model = HwActividad
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'estacion',
        'proyeccion',
        'parte',
        'lsm',
        'calculo_hw',
        'impactar',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )
