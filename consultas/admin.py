from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'nombre',
    'descripcion',
    'tipo_consulta',
    'contenido',
    
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'nombre', 'tipo_consulta']
