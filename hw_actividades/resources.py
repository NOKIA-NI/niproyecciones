from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import HwActividad
from .models import Proyeccion, ProyeccionExtra
from estaciones.models import Estacion
from partes.models import Parte


class HwActividadResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'site_name'))
    region = fields.Field(
        column_name='region',
        attribute='estacion__region')
    bolsa = fields.Field(
        column_name='bolsa',
        attribute='estacion__bolsa')
    comunidades = fields.Field(
        column_name='comunidades',
        attribute='estacion__comunidades')
    satelital = fields.Field(
        column_name='satelital',
        attribute='estacion__satelital')
    w_fc_imp = fields.Field(
        column_name='w_fc_imp',
        attribute='estacion__w_fc_imp')
    w_fc_sal = fields.Field(
        column_name='w_fc_sal',
        attribute='estacion__w_fc_sal')
    # proyeccion = fields.Field(
    #     column_name='proyeccion',
    #     attribute='proyeccion',
    #     widget=ForeignKeyWidget(Proyeccion, 'pk'))
    # proyeccion_extra = fields.Field(
    #     column_name='proyeccion',
    #     attribute='proyeccion',
    #     widget=ForeignKeyWidget(ProyeccionExtra, 'pk'))
    proyecto = fields.Field(
        column_name='proyecto')
    escenario = fields.Field(
        column_name='escenario')
    banda = fields.Field(
        column_name='banda')
    agrupadores = fields.Field(
        column_name='agrupadores')
    rfe = fields.Field(
        column_name='rfe')
    estado_proyeccion = fields.Field(
        column_name='estado_proyeccion')
    cantidad_estimada = fields.Field(
        column_name='cantidad_estimada')
    parte = fields.Field(
        column_name='parte',
        attribute='parte',
        widget=ForeignKeyWidget(Parte, 'parte_nokia'))
    grupo_parte = fields.Field(
        column_name='grupo_parte',
        attribute='parte__grupo_parte')

    class Meta:
        model = HwActividad
        exclude = ('estado', 'creado', 'actualizado',)
        export_order = (
        'id',
        'estacion',
        'region',
        'bolsa',
        'comunidades',
        'satelital',
        'w_fc_imp',
        'w_fc_sal',
        # 'proyeccion',
        # 'proyeccion_extra',
        'proyecto',
        'escenario',
        'banda',
        'agrupadores',
        'rfe',
        'estado_proyeccion',
        'cantidad_estimada',
        'parte',
        'grupo_parte',
        'lsm',
        'calculo_hw',
        'impactar',
        'cambiar_impactar',
        # 'estado',
        'subestado',
        # 'creado',
        # 'actualizado',
        )

    def dehydrate_proyecto(self, obj):
        try:
            if obj.proyeccion_extra.proyecto is not None:
                return obj.proyeccion_extra.proyecto
        except:
            return obj.proyeccion.proyecto

    def dehydrate_escenario(self, obj):
        try:
            if obj.proyeccion_extra.escenario is not None:
                return obj.proyeccion_extra.escenario
        except:
            return obj.proyeccion.escenario

    def dehydrate_banda(self, obj):
        try:
            if obj.proyeccion_extra.banda is not None:
                return obj.proyeccion_extra.banda
        except:
            return obj.proyeccion.banda

    def dehydrate_agrupadores(self, obj):
        try:
            if obj.proyeccion_extra.agrupadores is not None:
                return obj.proyeccion_extra.agrupadores
        except:
            return obj.proyeccion.agrupadores

    def dehydrate_rfe(self, obj):
        try:
            if obj.proyeccion_extra.rfe is not None:
                return obj.proyeccion_extra.rfe
        except:
            return obj.proyeccion.rfe

    def dehydrate_estado_proyeccion(self, obj):
        try:
            if obj.proyeccion_extra.estado_proyeccion is not None:
                return obj.proyeccion_extra.estado_proyeccion
        except:
            return obj.proyeccion.estado_proyeccion

    def dehydrate_cantidad_estimada(self, obj):
        try:
            if obj.proyeccion_extra.cantidad_estimada is not None:
                return obj.proyeccion_extra.cantidad_estimada
        except:
            return obj.proyeccion.cantidad_estimada
