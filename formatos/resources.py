from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget, ManyToManyWidget
from .models import FormatoEstacion, FormatoParte, FormatoClaro
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

class FormatoClaroResource(resources.ModelResource):
    sitio = fields.Field(
        column_name='sitio',
        attribute='sitio',
        widget=ForeignKeyWidget(Estacion, 'site_name'))

    class Meta:
        model = FormatoClaro
        exclude = ('formato_parte', 'estado', 'actualizado',)
        export_order = (
        'id',
        'sitio',
        'proyecto',
        'sap',
        'descripcion',
        'qty',
        'ciudad',
        'regional',
        'semana',
        'mes',
        # 'estado',
        'subestado',
        'creado',
        # 'actualizado',
        )