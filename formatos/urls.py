from django.urls import path
from .views import (
ListFormatoEstacion,
SearchFormatoEstacion,
FilterFormatoEstacion,
export_formato_estacion,
create_formato_estacion,

ListFormatoParte,
SearchFormatoParte,
FilterFormatoParte,
export_formato_parte,
create_formato_parte,

ListFormatoClaro,
SearchFormatoClaro,
FilterFormatoClaro,
export_formato_claro,
create_formato_claro,

ListFormatoClaroTotal,
SearchFormatoClaroTotal,
FilterFormatoClaroTotal,
export_formato_claro_total,
create_formato_claro_total,
)

app_name = 'formatos'

urlpatterns = [
    path('list/formato/estacion/', ListFormatoEstacion.as_view(), name='list_formato_estacion'),
    path('search/formato/estacion/', SearchFormatoEstacion.as_view(), name='search_formato_estacion'),
    path('filter/formato/estacion/', FilterFormatoEstacion.as_view(), name='filter_formato_estacion'),
    path('export/formato/estacion/', export_formato_estacion, name='export_formato_estacion'),
    path('create/formato/estacion/', create_formato_estacion, name='create_formato_formato/estacion'),

    path('list/formato/parte/', ListFormatoParte.as_view(), name='list_formato_parte'),
    path('search/formato/parte/', SearchFormatoParte.as_view(), name='search_formato_parte'),
    path('filter/formato/parte/', FilterFormatoParte.as_view(), name='filter_formato_parte'),
    path('export/formato/parte/', export_formato_parte, name='export_formato_parte'),
    path('create/formato/parte/', create_formato_parte, name='create_formato_parte'),

    path('list/formato/claro/', ListFormatoClaro.as_view(), name='list_formato_claro'),
    path('search/formato/claro/', SearchFormatoClaro.as_view(), name='search_formato_claro'),
    path('filter/formato/claro/', FilterFormatoClaro.as_view(), name='filter_formato_claro'),
    path('export/formato/claro/', export_formato_claro, name='export_formato_claro'),
    path('create/formato/claro/', create_formato_claro, name='create_formato_claro'),

    path('list/formato/claro/total/', ListFormatoClaroTotal.as_view(), name='list_formato_claro_total'),
    path('search/formato/claro/total/', SearchFormatoClaroTotal.as_view(), name='search_formato_claro_total'),
    path('filter/formato/claro/total/', FilterFormatoClaroTotal.as_view(), name='filter_formato_claro_total'),
    path('export/formato/claro/total/', export_formato_claro_total, name='export_formato_claro_total'),
    path('create/formato/claro/total/', create_formato_claro_total, name='create_formato_claro_total'),
]