from django.urls import path
from .views import (
ListEstacion,
DetailEstacion,
CreateEstacion,
UpdateEstacion,
DeleteEstacion,
SearchEstacion,
FilterEstacion,
export_estacion,
CronogramaFcImpEstacion,
CronogramaFcSalEstacion,
export_cronograma_estacion,

create_hw_estacion,
update_hw_estacion,
delete_hw_estacion,

ListBitacoraEstacion,
DetailBitacoraEstacion,
CreateBitacoraEstacion,
UpdateBitacoraEstacion,
DeleteBitacoraEstacion,
SearchBitacoraEstacion,
FilterBitacoraEstacion,
export_bitacora_estacion,

ListProyeccionEstacion,
DetailProyeccionEstacion,
CreateProyeccionEstacion,
UpdateProyeccionEstacion,
DeleteProyeccionEstacion,
SearchProyeccionEstacion,
FilterProyeccionEstacion,
export_proyeccion_estacion,
)

app_name = 'estaciones'

urlpatterns = [
    path('list/estacion/', ListEstacion.as_view(), name='list_estacion'),
    path('detail/estacion/<int:pk>/', DetailEstacion.as_view(), name='detail_estacion'),
    path('create/estacion/', CreateEstacion.as_view(), name='create_estacion'),
    path('update/estacion/<int:pk>/', UpdateEstacion.as_view(), name='update_estacion'),
    path('delete/estacion/<int:pk>/', DeleteEstacion.as_view(), name='delete_estacion'),
    path('search/estacion/', SearchEstacion.as_view(), name='search_estacion'),
    path('filter/estacion/', FilterEstacion.as_view(), name='filter_estacion'),
    path('export/estacion/', export_estacion, name='export_estacion'),
    path('cronograma/fc/imp/estacion/', CronogramaFcImpEstacion.as_view(), name='cronograma_fc_imp_estacion'),
    path('cronograma/fc/sal/estacion/', CronogramaFcSalEstacion.as_view(), name='cronograma_fc_sal_estacion'),
    path('export/cronograma/estacion/', export_cronograma_estacion, name='export_cronograma_estacion'),

    path('create/hw/estacion/', create_hw_estacion, name='create_hw_estacion'),
    path('update/hw/estacion/', update_hw_estacion, name='update_hw_estacion'),
    path('delete/hw/estacion/', delete_hw_estacion, name='delete_hw_estacion'),

    path('list/bitacora/estacion/', ListBitacoraEstacion.as_view(), name='list_bitacora_estacion'),
    path('detail/bitacora/estacion/<int:pk>/', DetailBitacoraEstacion.as_view(), name='detail_bitacora_estacion'),
    path('create/bitacora/estacion/', CreateBitacoraEstacion.as_view(), name='create_bitacora_estacion'),
    path('update/bitacora/estacion/<int:pk>/', UpdateBitacoraEstacion.as_view(), name='update_bitacora_estacion'),
    path('delete/bitacora/estacion/<int:pk>/', DeleteBitacoraEstacion.as_view(), name='delete_bitacora_estacion'),
    path('search/bitacora/estacion/', SearchBitacoraEstacion.as_view(), name='search_bitacora_estacion'),
    path('filter/bitacora/estacion/', FilterBitacoraEstacion.as_view(), name='filter_bitacora_estacion'),
    path('export/bitacora/estacion/', export_bitacora_estacion, name='export_bitacora_estacion'),

    path('list/proyeccion/estacion/', ListProyeccionEstacion.as_view(), name='list_proyeccion_estacion'),
    path('detail/proyeccion/estacion/<int:pk>/', DetailProyeccionEstacion.as_view(), name='detail_proyeccion_estacion'),
    path('create/proyeccion/estacion/', CreateProyeccionEstacion.as_view(), name='create_proyeccion_estacion'),
    path('update/proyeccion/estacion/<int:pk>/', UpdateProyeccionEstacion.as_view(), name='update_proyeccion_estacion'),
    path('delete/proyeccion/estacion/<int:pk>/', DeleteProyeccionEstacion.as_view(), name='delete_proyeccion_estacion'),
    path('search/proyeccion/estacion/', SearchProyeccionEstacion.as_view(), name='search_proyeccion_estacion'),
    path('filter/proyeccion/estacion/', FilterProyeccionEstacion.as_view(), name='filter_proyeccion_estacion'),
    path('export/proyeccion/estacion/', export_proyeccion_estacion, name='export_proyeccion_estacion'),
]
