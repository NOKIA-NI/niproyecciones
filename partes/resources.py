from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import Parte

class ParteResource(resources.ModelResource):

    class Meta:
        model = Parte
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'cod_sap',
        'parte_nokia',
        'capex',
        'grupo_parte',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )
