from django.urls import path
from .views import (
ListExistencia,
DetailExistencia,
CreateExistencia,
UpdateExistencia,
DeleteExistencia,
SearchExistencia,
export_existencia,
calculate_existencia,
)

app_name = 'existencias'

urlpatterns = [
    path('list/existencia/', ListExistencia.as_view(), name='list_existencia'),
    path('detail/existencia/<int:pk>/', DetailExistencia.as_view(), name='detail_existencia'),
    path('create/existencia/', CreateExistencia.as_view(), name='create_existencia'),
    path('update/existencia/<int:pk>/', UpdateExistencia.as_view(), name='update_existencia'),
    path('delete/existencia/<int:pk/', DeleteExistencia.as_view(), name='delete_existencia'),
    path('search/existencia/', SearchExistencia.as_view(), name='search_existencia'),
    path('export/existencia/', export_existencia, name='export_existencia'),
    path('calculate/existencia/', calculate_existencia, name='calculate_existencia'),
]
