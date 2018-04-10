from django.contrib import admin

from .models import Llegada
from import_export.admin import ImportExportModelAdmin
from .resources import LlegadaResource

#@admin.register(Llegada)
#class LlegadaAdmin(admin.ModelAdmin):
#    pass

@admin.register(Llegada)
class LlegadaAdmin(ImportExportModelAdmin):
    resource_class = LlegadaResource
    list_display = (
    'id',
    'parte',
    'grupo_parte',
    'w14',
    'w15',
    'w16',
    'w17',
    'w18',
    'w19',
    'w20',
    'w21',
    'w22',
    'w23',
    'w24',
    'w25',
    'w26',
    'w27',
    'w28',
    'w29',
    'w30',
    'w31',
    'w32',
    'w33',
    'w34',
    'w35',
    'w36',
    'w37',
    'w38',
    'w39',
    'w40',
    'w41',
    'w42',
    'w43',
    'w44',
    'w45',
    'w46',
    'w47',
    'w48',
    'w49',
    'w50',
    'w51',
    'w52',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('estado', 'subestado', 'creado', 'actualizado')
    search_fields = ['id', 'parte']
