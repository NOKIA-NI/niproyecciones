from django.urls import path
from .views import (
ListConsulta,
DetailConsulta,
CreateConsulta,
UpdateConsulta,
DeleteConsulta,
SearchConsulta,
FilterConsulta,
)

app_name = 'consultas'

urlpatterns = [
    path('list/consulta/', ListConsulta.as_view(), name='list_consulta'),
    path('detail/consulta/<int:pk>/', DetailConsulta.as_view(), name='detail_consulta'),
    path('create/consulta/', CreateConsulta.as_view(), name='create_consulta'),
    path('update/consulta/<int:pk>/', UpdateConsulta.as_view(), name='update_consulta'),
    path('delete/consulta/<int:pk>/', DeleteConsulta.as_view(), name='delete_consulta'),
    path('search/consulta/', SearchConsulta.as_view(), name='search_consulta'),
    path('filter/consulta/', FilterConsulta.as_view(), name='filter_consulta'),
]
