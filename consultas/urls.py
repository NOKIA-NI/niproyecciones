from django.urls import path
from .views import (
ConsultaView,
)

app_name = 'consultas'

urlpatterns = [
    path('list/consulta', ConsultaView.as_view(), name='list_consulta'),
]
