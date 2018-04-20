from django.urls import path
from .views import (
create_impacto,
calcular_impacto,
)

app_name = 'impactos'

urlpatterns = [
    path('create/impacto/', create_impacto, name='create_impacto'),
    path('calcular/impacto/', calcular_impacto, name='calcular_impacto'),
]
