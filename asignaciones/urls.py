from django.urls import path
from .views import (
ListAsignacionBulk,
CreateAsignacionBulk,
UpdateAsignacionBulk,
DeleteAsignacionBulk,
SearchAsignacionBulk,
FilterAsignacionBulk,
export_asignacion_bulk,

ListAsignacionAntena,
CreateAsignacionAntena,
UpdateAsignacionAntena,
DeleteAsignacionAntena,
SearchAsignacionAntena,
FilterAsignacionAntena,
export_asignacion_antena,

ListEstadoPo,
CreateEstadoPo,
UpdateEstadoPo,
DeleteEstadoPo,
SearchEstadoPo,
FilterEstadoPo,
export_estado_po,
)

app_name = 'asignaciones'

urlpatterns = [
    path('list/asignacion/bulk/', ListAsignacionBulk.as_view(), name='list_asignacion_bulk'),
    path('create/asignacion/bulk/', CreateAsignacionBulk.as_view(), name='create_asignacion_bulk'),
    path('update/asignacion/bulk/', UpdateAsignacionBulk.as_view(), name='update_asignacion_bulk'),
    path('delete/asignacion/bulk/', DeleteAsignacionBulk.as_view(), name='delete_asignacion_bulk'),
    path('search/asignacion/bulk/', SearchAsignacionBulk.as_view(), name='search_asignacion_bulk'),
    path('filter/asignacion/bulk/', FilterAsignacionBulk.as_view(), name='filter_asignacion_bulk'),
    path('export/asignacion/bulk/', export_asignacion_bulk, name='export_asignacion_bulk'),

    path('list/asignacion/antena/', ListAsignacionAntena.as_view(), name='list_asignacion_antena'),
    path('create/asignacion/antena/', CreateAsignacionAntena.as_view(), name='create_asignacion_antena'),
    path('update/asignacion/antena/', UpdateAsignacionAntena.as_view(), name='update_asignacion_antena'),
    path('delete/asignacion/antena/', DeleteAsignacionAntena.as_view(), name='delete_asignacion_antena'),
    path('search/asignacion/antena/', SearchAsignacionAntena.as_view(), name='search_asignacion_antena'),
    path('filter/asignacion/antena/', FilterAsignacionAntena.as_view(), name='filter_asignacion_antena'),
    path('export/asignacion/antena/', export_asignacion_antena, name='export_asignacion_antena'),

    path('list/estado/po/', ListEstadoPo.as_view(), name='list_estado_po'),
    path('create/estado/po/', CreateEstadoPo.as_view(), name='create_estado_po'),
    path('update/estado/po/', UpdateEstadoPo.as_view(), name='update_estado_po'),
    path('delete/estado/po/', DeleteEstadoPo.as_view(), name='delete_estado_po'),
    path('search/estado/po/', SearchEstadoPo.as_view(), name='search_estado_po'),
    path('filter/estado/po/', FilterEstadoPo.as_view(), name='filter_estado_po'),
    path('export/estado/po/', export_estado_po, name='export_estado_po'),
]