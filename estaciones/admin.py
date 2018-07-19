from django.contrib import admin

from .models import Estacion, BitacoraEstacion, ProyeccionEstacion
from import_export.admin import ImportExportModelAdmin
from .resources import EstacionResource, BitacoraEstacionResource, ProyeccionEstacionResource

#@admin.register(Estacion)
#class EstacionAdmin(admin.ModelAdmin):
#    pass

@admin.register(Estacion)
class EstacionAdmin(ImportExportModelAdmin):
    resource_class = EstacionResource
    list_display = (
    'id',
    'site_name',
    'region',
    'ciudad',
    'scope_claro',
    'w_fc_sal',
    'w_fc_imp',
    'w_fc_c',
    'total_actividades',
    'estado_wr',
    'mos',
    'bolsa',
    'status_nokia',
    'comunidades',
    'satelital',
    'impactar',
    'list_partes',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'site_name']

    def list_partes(self, obj):
        return "\n".join([p.parte_nokia for p in obj.partes.all()])

@admin.register(BitacoraEstacion)
class BitacoraEstacionAdmin(ImportExportModelAdmin):
    resource_class = BitacoraEstacionResource
    list_display = (
    'id',
    'estacion',
    'fecha_bitacora',
    'observaciones',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion__site_name']

@admin.register(ProyeccionEstacion)
class ProyeccionEstacionAdmin(ImportExportModelAdmin):
    resource_class = ProyeccionEstacionResource
    list_display = (
    'id',
    'estacion',
    'proyeccion',
    'fecha_proyeccion',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion__site_name']
