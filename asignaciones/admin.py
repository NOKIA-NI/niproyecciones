from django.contrib import admin

from .models import (
    AsignacionBulk,
    AsignacionAntena,
    EstadoPo,
    PoZina,
    SitioBolsa,
    SitioBulk,
    SitioPo,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
    AsignacionBulkResource,
    AsignacionAntenaResource,
    EstadoPoResource,
    PoZinaResource,
    SitioBolsaResource,
    SitioBulkResource,
    SitioPoResource,
)

@admin.register(AsignacionBulk)
class AsignacionBulkAdmin(ImportExportModelAdmin):
    resource_class = AsignacionBulkResource
    list_display = (
    'id',
    'parte',
    'cod_sap',
    'capex',
    'cantidad',
    'cod_bodega',
    'bodega',
    'comentario_bodega',
    'so',
    'po',
    
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'parte__parte_nokia']

@admin.register(AsignacionAntena)
class AsignacionAntenaAdmin(ImportExportModelAdmin):
    resource_class = AsignacionAntenaResource
    list_display = (
    'id',
    'parte',
    'cod_sap',
    'capex',
    'cantidad',
    'cod_bodega',
    'bodega',
    'comentario_bodega',
    'so',
    'po',
    'familia',
    'caracteristicas',
    'puertos',
    
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'parte__parte_nokia']

@admin.register(EstadoPo)
class EstadoPoAdmin(ImportExportModelAdmin):
    resource_class = EstadoPoResource
    list_display = (
    'id',
    'numero_po',
    'estacion',
    'project',
    'bts',
    'bts_status',
    'bts_arrival_week',
    'jumper',
    'jumper_status',
    'jumper_arrival_week',
    'fxcb',
    'fxcb_status',
    'customs_ceared',
    'sr',
    'awb',
    'eta',
    'delivery',
    'pre_pgi',
    'fc_impl',
    'fxcb_qty',
    'annotation',
    'comprometido',
    'share',
    'w_reviewed',
    'columna_924',
    
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion']

@admin.register(PoZina)
class PoZinaAdmin(ImportExportModelAdmin):
    resource_class = PoZinaResource
    list_display = (
    'id',
    'cpo_number',
    'so_jumper',
    'so_bts',
    'project',
    'site_name',
    'material_description',
    'parte_capex',
    'quantity',
    
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'cpo_number', 'site_name', 'parte_capex']

@admin.register(SitioBolsa)
class SitioBolsaAdmin(ImportExportModelAdmin):
    resource_class = SitioBolsaResource
    list_display = (
    'id',
    'estacion',
    
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion.site_name']

@admin.register(SitioBulk)
class SitioBulkAdmin(ImportExportModelAdmin):
    resource_class = SitioBulkResource
    list_display = (
    'id',
    'estacion',
    
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion.site_name']

@admin.register(SitioPo)
class SitioPoAdmin(ImportExportModelAdmin):
    resource_class = SitioPoResource
    list_display = (
    'id',
    'numero_po',
    'estacion',
    'bts',
    'bts_status',
    'jumper',
    'jumper_status',
    'fxcb',
    'fxcb_status',
    
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'estacion.site_name']