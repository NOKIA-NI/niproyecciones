from django.urls import path
from .views import (
DashboardView,
TaskView,
impactos,
cronograma_bolsas,
cronograma_status_nokia,
impactos_grupo_parte,
impactos_parte,
)

app_name = 'dashboard'

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('task', TaskView.as_view(), name='task'),
    path('impactos', impactos, name='impactos'),
    path('cronograma/bolsas', cronograma_bolsas, name='cronograma_bolsas'),
    path('cronograma/status/nokia', cronograma_status_nokia, name='cronograma_status_nokia'),
    path('impactos/grupo/parte', impactos_grupo_parte, name='impactos_grupo_parte'),
    path('impactos/parte', impactos_parte, name='impactos_parte'),
]
