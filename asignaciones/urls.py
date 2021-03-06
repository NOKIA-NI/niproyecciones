from django.urls import path
from .views import (
ListAsignacionBulk,
DetailAsignacionBulk,
CreateAsignacionBulk,
UpdateAsignacionBulk,
DeleteAsignacionBulk,
SearchAsignacionBulk,
FilterAsignacionBulk,
export_asignacion_bulk,

ListAsignacionAntena,
DetailAsignacionAntena,
CreateAsignacionAntena,
UpdateAsignacionAntena,
DeleteAsignacionAntena,
SearchAsignacionAntena,
FilterAsignacionAntena,
export_asignacion_antena,

ListEstadoPo,
DetailEstadoPo,
CreateEstadoPo,
UpdateEstadoPo,
DeleteEstadoPo,
SearchEstadoPo,
FilterEstadoPo,
export_estado_po,

ListPoZina,
DetailPoZina,
CreatePoZina,
UpdatePoZina,
DeletePoZina,
SearchPoZina,
FilterPoZina,
export_po_zina,

ListEstadoAntena,
DetailEstadoAntena,
CreateEstadoAntena,
UpdateEstadoAntena,
DeleteEstadoAntena,
SearchEstadoAntena,
FilterEstadoAntena,
export_estado_antena,

sitios_asignacion,
sitios_po,
asignacion_bolsa,
sobrantes,
asignacion_bulk,
)

app_name = 'asignaciones'

urlpatterns = [
    path('list/asignacion/bulk/', ListAsignacionBulk.as_view(), name='list_asignacion_bulk'),
    path('detail/asignacion/bulk/<int:pk>/', DetailAsignacionBulk.as_view(), name='detail_asignacion_bulk'),
    path('create/asignacion/bulk/', CreateAsignacionBulk.as_view(), name='create_asignacion_bulk'),
    path('update/asignacion/bulk/<int:pk>/', UpdateAsignacionBulk.as_view(), name='update_asignacion_bulk'),
    path('delete/asignacion/bulk/<int:pk>/', DeleteAsignacionBulk.as_view(), name='delete_asignacion_bulk'),
    path('search/asignacion/bulk/', SearchAsignacionBulk.as_view(), name='search_asignacion_bulk'),
    path('filter/asignacion/bulk/', FilterAsignacionBulk.as_view(), name='filter_asignacion_bulk'),
    path('export/asignacion/bulk/', export_asignacion_bulk, name='export_asignacion_bulk'),

    path('list/asignacion/antena/', ListAsignacionAntena.as_view(), name='list_asignacion_antena'),
    path('detail/asignacion/antena/<int:pk>/', DetailAsignacionAntena.as_view(), name='detail_asignacion_antena'),
    path('create/asignacion/antena/', CreateAsignacionAntena.as_view(), name='create_asignacion_antena'),
    path('update/asignacion/antena/<int:pk>/', UpdateAsignacionAntena.as_view(), name='update_asignacion_antena'),
    path('delete/asignacion/antena/<int:pk>/', DeleteAsignacionAntena.as_view(), name='delete_asignacion_antena'),
    path('search/asignacion/antena/', SearchAsignacionAntena.as_view(), name='search_asignacion_antena'),
    path('filter/asignacion/antena/', FilterAsignacionAntena.as_view(), name='filter_asignacion_antena'),
    path('export/asignacion/antena/', export_asignacion_antena, name='export_asignacion_antena'),

    path('list/estado/po/', ListEstadoPo.as_view(), name='list_estado_po'),
    path('detail/estado/po/<int:pk>/', DetailEstadoPo.as_view(), name='detail_estado_po'),
    path('create/estado/po/', CreateEstadoPo.as_view(), name='create_estado_po'),
    path('update/estado/po/<int:pk>/', UpdateEstadoPo.as_view(), name='update_estado_po'),
    path('delete/estado/po/<int:pk>/', DeleteEstadoPo.as_view(), name='delete_estado_po'),
    path('search/estado/po/', SearchEstadoPo.as_view(), name='search_estado_po'),
    path('filter/estado/po/', FilterEstadoPo.as_view(), name='filter_estado_po'),
    path('export/estado/po/', export_estado_po, name='export_estado_po'),

    path('list/po/zina/', ListPoZina.as_view(), name='list_po_zina'),
    path('detail/po/zina/<int:pk>/', DetailPoZina.as_view(), name='detail_po_zina'),
    path('create/po/zina/', CreatePoZina.as_view(), name='create_po_zina'),
    path('update/po/zina/<int:pk>/', UpdatePoZina.as_view(), name='update_po_zina'),
    path('delete/po/zina/<int:pk>/', DeletePoZina.as_view(), name='delete_po_zina'),
    path('search/po/zina/', SearchPoZina.as_view(), name='search_po_zina'),
    path('filter/po/zina/', FilterPoZina.as_view(), name='filter_po_zina'),
    path('export/po/zina/', export_po_zina, name='export_po_zina'),

    path('list/estado/antena/', ListEstadoAntena.as_view(), name='list_estado_antena'),
    path('detail/estado/antena/<int:pk>/', DetailEstadoAntena.as_view(), name='detail_estado_antena'),
    path('create/estado/antena/', CreateEstadoAntena.as_view(), name='create_estado_antena'),
    path('update/estado/antena/<int:pk>/', UpdateEstadoAntena.as_view(), name='update_estado_antena'),
    path('delete/estado/antena/<int:pk>/', DeleteEstadoAntena.as_view(), name='delete_estado_antena'),
    path('search/estado/antena/', SearchEstadoAntena.as_view(), name='search_estado_antena'),
    path('filter/estado/antena/', FilterEstadoAntena.as_view(), name='filter_estado_antena'),
    path('exestadort/estado/antena/', export_estado_antena, name='export_estado_antena'),

    path('sitios/asignacion/', sitios_asignacion, name='sitios_asignacion'),
    path('sitios/po/', sitios_po, name='sitios_po'),
    path('asignacion/bolsa/', asignacion_bolsa, name='asignacion_bolsa'),
    path('sobrantes/', sobrantes, name='sobrantes'),
    path('asignacion/bulk/', asignacion_bulk, name='asignacion_bulk'),
]