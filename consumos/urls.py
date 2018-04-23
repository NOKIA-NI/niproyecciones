from django.urls import path
from .views import (
ListConsumoNokia,
DetailConsumoNokia,
CreateConsumoNokia,
UpdateConsumoNokia,
DeleteConsumoNokia,
SearchConsumoNokia,
export_consumo_nokia,
calculate_consumo_nokia,

ListConsumoClaro,
DetailConsumoClaro,
CreateConsumoClaro,
UpdateConsumoClaro,
DeleteConsumoClaro,
SearchConsumoClaro,
export_consumo_claro,
)

app_name = 'consumos'

urlpatterns = [
    path('list/consumo/nokia/', ListConsumoNokia.as_view(), name='list_consumo_nokia'),
    path('detail/consumo/nokia/<int:pk>/', DetailConsumoNokia.as_view(), name='detail_consumo_nokia'),
    path('create/consumo/nokia/', CreateConsumoNokia.as_view(), name='create_consumo_nokia'),
    path('update/consumo/nokia/<int:pk>/', UpdateConsumoNokia.as_view(), name='update_consumo_nokia'),
    path('delete/consumo/nokia/<int:pk/', DeleteConsumoNokia.as_view(), name='delete_consumo_nokia'),
    path('search/consumo/nokia/', SearchConsumoNokia.as_view(), name='search_consumo_nokia'),
    path('export/consumo/nokia/', export_consumo_nokia, name='export_consumo_nokia'),
    path('calculate/consumo/nokia/', calculate_consumo_nokia, name='calculate_consumo_nokia'),

    path('list/consumo/claro/', ListConsumoClaro.as_view(), name='list_consumo_claro'),
    path('detail/consumo/claro/<int:pk>/', DetailConsumoClaro.as_view(), name='detail_consumo_claro'),
    path('create/consumo/claro/', CreateConsumoClaro.as_view(), name='create_consumo_claro'),
    path('update/consumo/claro/<int:pk>/', UpdateConsumoClaro.as_view(), name='update_consumo_claro'),
    path('delete/consumo/claro/<int:pk/', DeleteConsumoClaro.as_view(), name='delete_consumo_claro'),
    path('search/consumo/claro/', SearchConsumoClaro.as_view(), name='search_consumo_claro'),
    path('export/consumo/claro/', export_consumo_claro, name='export_consumo_claro'),
]
