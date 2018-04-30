from django.urls import path
from .views import (
DashboardView,
impactos,
impactos_grupo_parte,
impactos_parte,
)

app_name = 'dashboard'

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('impactos', impactos, name='impactos'),
    path('impactos/grupo/parte', impactos_grupo_parte, name='impactos_grupo_parte'),
    path('impactos/parte', impactos_parte, name='impactos_parte'),
]
