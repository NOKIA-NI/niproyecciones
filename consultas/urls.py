from django.urls import path
from .views import (
ListConsulta,
DetailConsulta,
CreateConsulta,
)

app_name = 'consultas'

urlpatterns = [
    path('list/consulta', ListConsulta.as_view(), name='list_consulta'),
    path('detail/consulta', DetailConsulta.as_view(), name='detail_consulta'),
    path('create/consulta', CreateConsulta.as_view(), name='create_consulta'),
]
