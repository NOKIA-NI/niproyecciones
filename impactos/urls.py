from django.urls import path
from .views import (
ListImpacto,
export_impacto,
create_impacto,
calculate_impacto,
delete_impacto,
)

app_name = 'impactos'

urlpatterns = [
    path('list/impacto/', ListImpacto.as_view(), name='list_impacto'),
    path('export/impacto/', export_impacto, name='export_impacto'),
    path('create/impacto/', create_impacto, name='create_impacto'),
    path('calculate/impacto/', calculate_impacto, name='calculate_impacto'),
    path('delete/impacto/', delete_impacto, name='delete_impacto'),
]
