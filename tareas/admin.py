from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'descripcion',
        'ejecutar',
        'estado',
        'subestado',
        'creado',
        'actualizado',
        )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'nombre']
