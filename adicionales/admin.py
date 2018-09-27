from django.contrib import admin
from .models import (
    Adicional,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
    AdicionalResource,
)

@admin.register(Adicional)
class AdicionalAdmin(ImportExportModelAdmin):
    resource_class = AdicionalResource
    list_display = (
    'idadicionales_hw_sv',
    'wp',
    'siteName',
    'proyecto',
    'banda',
    'escenario',
    'tipo',
    'seccion',
    'parte',
    'cantidad',
    'proceso',
    'observaciones',
    'fecha_pedido',
    'usuario',
    'id',

    'recibido',
    'fecha_recibido',
    'responsable',
    'asignado',
    'fecha_asignado',
    'comentario',
    
    # 'estado',
    # 'subestado',
    # 'creado',
    # 'actualizado',
    )
    # list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['idadicionales_hw_sv', 'siteName', 'parte'] 
