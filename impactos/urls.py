from django.urls import path
from .views import (
ListImpacto,
SearchImpacto,
FilterImpacto,
export_impacto,
create_impacto,
calculate_impacto,
calculate_tipo_impacto,
delete_impacto,
)

app_name = 'impactos'

urlpatterns = [
    path('list/impacto/', ListImpacto.as_view(), name='list_impacto'),
    path('search/impacto/', SearchImpacto.as_view(), name='search_impacto'),
    path('filter/impacto/', FilterImpacto.as_view(), name='filter_impacto'),
    path('export/impacto/', export_impacto, name='export_impacto'),
    path('create/impacto/', create_impacto, name='create_impacto'),
    path('calculate/impacto/', calculate_impacto, name='calculate_impacto'),
    path('calculate/tipo/impacto/', calculate_tipo_impacto, name='calculate_tipo_impacto'),
    path('delete/impacto/', delete_impacto, name='delete_impacto'),
]
