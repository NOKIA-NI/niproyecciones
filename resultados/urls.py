from django.urls import path
from .views import (
ListResultado,
DetailResultado,
CreateResultado,
UpdateResultado,
DeleteResultado,
SearchResultado,
export_resultado,
calculate_resultado,
)

app_name = 'resultados'

urlpatterns = [
    path('list/resultado/', ListResultado.as_view(), name='list_resultado'),
    path('detail/resultado/<int:pk>/', DetailResultado.as_view(), name='detail_resultado'),
    path('create/resultado/', CreateResultado.as_view(), name='create_resultado'),
    path('update/resultado/<int:pk>/', UpdateResultado.as_view(), name='update_resultado'),
    path('delete/resultado/<int:pk/', DeleteResultado.as_view(), name='delete_resultado'),
    path('search/resultado/', SearchResultado.as_view(), name='search_resultado'),
    path('export/resultado/', export_resultado, name='export_resultado'),
    path('calculate/resultado/', calculate_resultado, name='calculate_resultado'),
]
