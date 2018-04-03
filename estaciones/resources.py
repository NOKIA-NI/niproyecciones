from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import Estacion

class EstacionResource(resources.ModelResource):

    class Meta:
        model = Estacion
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'site_name',
        'region',
        'scope_claro',
        'w_fc_imp',
        'total_actividades',
        'estado_wr',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )
