from django.urls import path
from .views import (
ListEstacion,
DetailEstacion,
CreateEstacion,
UpdateEstacion,
DeleteEstacion,
SearchEstacion,
export_estacion,
CronogramaFcImpEstacion,
CronogramaFcSalEstacion,
)

app_name = 'estaciones'

urlpatterns = [
    path('list/estacion/', ListEstacion.as_view(), name='list_estacion'),
    path('detail/estacion/<int:pk>/', DetailEstacion.as_view(), name='detail_estacion'),
    path('create/estacion/', CreateEstacion.as_view(), name='create_estacion'),
    path('update/estacion/<int:pk>/', UpdateEstacion.as_view(), name='update_estacion'),
    path('delete/estacion/<int:pk/', DeleteEstacion.as_view(), name='delete_estacion'),
    path('search/estacion/', SearchEstacion.as_view(), name='search_estacion'),
    path('export/estacion/', export_estacion, name='export_estacion'),
    path('cronograma/fc/imp/estacion/', CronogramaFcImpEstacion.as_view(), name='cronograma_fc_imp_estacion'),
    path('cronograma/fc/sal/estacion/', CronogramaFcSalEstacion.as_view(), name='cronograma_fc_sal_estacion'),
]
