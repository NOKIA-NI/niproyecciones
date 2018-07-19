from import_export import resources, fields
from import_export.widgets import (
    ForeignKeyWidget,
    DateWidget,
    DateTimeWidget,
    IntegerWidget,
    ManyToManyWidget,
    )
from .models import (
    FormatoEstacion,
    FormatoParte,
    FormatoClaro,
    FormatoClaroTotal,
    FormatoClaroKit,
    FormatoParteInput,
    FormatoParteDelta,
    )
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
    formato_parte = fields.Field(
        column_name='formato_parte',
        attribute='formato_parte',
        widget=ForeignKeyWidget(FormatoParte, 'parte'))

    class Meta:
        model = FormatoClaro
        exclude = ('estado', 'subestado', 'creado', 'actualizado',)
        export_order = (
        'id', 
        'id_sitio',
        'sitio',
        'proyecto',
        'formato_parte',
        'sap',
        'descripcion',
        'qty',
        'ciudad',
        'regional',
        'semana',
        'mes',
        'generado',
        # 'estado',
        # 'subestado',
        # 'creado',
        # 'actualizado',
        )

class FormatoClaroTotalResource(resources.ModelResource):
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = FormatoClaroTotal
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'parte',
        'cod_sap',
        'capex',
        'grupo_parte',
        'total',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class FormatoClaroKitResource(resources.ModelResource):
    sitio = fields.Field(
        column_name='sitio',
        attribute='sitio',
        widget=ForeignKeyWidget(Estacion, 'site_name'))
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = FormatoClaroKit
        exclude = ('estado', 'subestado', 'creado', 'actualizado',)
        export_order = (
        'id', 
        'id_sitio',
        'sitio',
        'proyecto',
        'parte',
        'sap',
        'descripcion',
        'qty',
        'ciudad',
        'regional',
        'semana',
        'mes',
        'generado',
        # 'estado',
        # 'subestado',
        # 'creado',
        # 'actualizado',
        )

class FormatoParteInputResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'site_name'))
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = FormatoParteInput
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'estacion',
        'parte',
        'cantidad',
        'fecha_formato',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

class FormatoParteDeltaResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'site_name'))
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))

    class Meta:
        model = FormatoParteDelta
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'estacion',
        'parte',
        'cantidad_parte',
        'cantidad_input',
        'cantidad_delta',
        'fecha_formato',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )