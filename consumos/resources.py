from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import ConsumoNokia, ConsumoClaro
from partes.models import Parte

class ConsumoNokiaResource(resources.ModelResource):
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = ConsumoNokia
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'parte',
        'grupo_parte',
        'w14',
        'w15',
        'w16',
        'w17',
        'w18',
        'w19',
        'w20',
        'w21',
        'w22',
        'w23',
        'w24',
        'w25',
        'w26',
        'w27',
        'w28',
        'w29',
        'w30',
        'w31',
        'w32',
        'w33',
        'w34',
        'w35',
        'w36',
        'w37',
        'w38',
        'w39',
        'w40',
        'w41',
        'w42',
        'w43',
        'w44',
        'w45',
        'w46',
        'w47',
        'w48',
        'w49',
        'w50',
        'w51',
        'w52',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class ConsumoClaroResource(resources.ModelResource):
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = ConsumoClaro
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'parte',
        'w14',
        'w15',
        'w16',
        'w17',
        'w18',
        'w19',
        'w20',
        'w21',
        'w22',
        'w23',
        'w24',
        'w25',
        'w26',
        'w27',
        'w28',
        'w29',
        'w30',
        'w31',
        'w32',
        'w33',
        'w34',
        'w35',
        'w36',
        'w37',
        'w38',
        'w39',
        'w40',
        'w41',
        'w42',
        'w43',
        'w44',
        'w45',
        'w46',
        'w47',
        'w48',
        'w49',
        'w50',
        'w51',
        'w52',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )
