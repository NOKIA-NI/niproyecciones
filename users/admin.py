from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'user',
    'slug',
    'perfil',
    'nombre',
    'apellido',
    'nombre_completo',
    'email',
    'celular',
    'empresa',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
