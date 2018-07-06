from django.contrib import admin

from .models import Rastreo, Proceso

@admin.register(Rastreo)
class RastreoAdmin(admin.ModelAdmin):
   list_display = (
    'id',
    'responsable',
    'nombre',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )

@admin.register(Proceso)
class ProcesoAdmin(admin.ModelAdmin):
   list_display = (
    'id',
    'rastreo',
    'responsable',
    'tipo_proceso',
    'estado_proceso',
    'archivo',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
