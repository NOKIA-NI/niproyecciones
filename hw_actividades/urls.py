from django.urls import path
from .views import (
ListHwActividad,
DetailHwActividad,
CreateHwActividad,
UpdateHwActividad,
DeleteHwActividad,
SearchHwActividad,
FilterHwActividad,
export_hw_actividad
)

app_name = 'hw_actividades'

urlpatterns = [
    path('list/hw/actividad/', ListHwActividad.as_view(), name='list_hw_actividad'),
    path('detail/hw/actividad/<int:pk>/', DetailHwActividad.as_view(), name='detail_hw_actividad'),
    path('create/hw/actividad/', CreateHwActividad.as_view(), name='create_hw_actividad'),
    path('update/hw/actividad/<int:pk>/', UpdateHwActividad.as_view(), name='update_hw_actividad'),
    path('delete/hw/actividad/<int:pk/', DeleteHwActividad.as_view(), name='delete_hw_actividad'),
    path('search/hw/actividad/', SearchHwActividad.as_view(), name='search_hw_actividad'),
    path('filter/hw/actividad/', FilterHwActividad.as_view(), name='filter_hw_actividad'),
    path('export/hw/actividad/', export_hw_actividad, name='export_hw_actividad'),
]
