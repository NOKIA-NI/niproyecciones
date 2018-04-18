from django.urls import path
from .views import (
ListDisponible,
DetailDisponible,
CreateDisponible,
UpdateDisponible,
DeleteDisponible,
SearchDisponible,
export_disponible,
calcular_disponible,
)

app_name = 'disponibles'

urlpatterns = [
    path('list/disponible/', ListDisponible.as_view(), name='list_disponible'),
    path('detail/disponible/<int:pk>/', DetailDisponible.as_view(), name='detail_disponible'),
    path('create/disponible/', CreateDisponible.as_view(), name='create_disponible'),
    path('update/disponible/<int:pk>/', UpdateDisponible.as_view(), name='update_disponible'),
    path('delete/disponible/<int:pk/', DeleteDisponible.as_view(), name='delete_disponible'),
    path('search/disponible/', SearchDisponible.as_view(), name='search_disponible'),
    path('export/disponible/', export_disponible, name='export_disponible'),
    path('calcular/disponible/', calcular_disponible, name='calcular_disponible'),
]
