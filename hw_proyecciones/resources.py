from import_export import resources
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from .models import HwProyeccion, HwEstacion, HwParte

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

class HwEstacionResource(resources.ModelResource):

    class Meta:
        model = HwEstacion
        # exclude = ('id',)
        export_order = (
        'id',
        'siteName',
        'region',
        'scope_claro',
        'proyeccion_instalacion',
        'w_proyeccion_instalacion',
        'actividades',
        'bolsa',
        )

class HwParteResource(resources.ModelResource):

    class Meta:
        model = HwParte
        # exclude = ('id',)
        export_order = (
        'id',
        'cod_capex',
        'nombre_nokia',
        'nombre_capex',
        'seccion_parte',
        )
