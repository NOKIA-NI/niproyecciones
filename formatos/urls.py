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
]