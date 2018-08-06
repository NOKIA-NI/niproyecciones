from django.contrib import admin
from .models import Tarea, GrupoTarea

@admin.register(GrupoTarea)
class GrupoTareaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'descripcion',
        'estado',
        'subestado',
        'creado',
        'actualizado',
        )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'nombre']

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'descripcion',
        'grupo_tarea',
        'ejecutar',
        'tarea_id',
        'estado',
        'subestado',
        'creado',
        'actualizado',
        )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'nombre']
