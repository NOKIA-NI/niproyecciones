from django.urls import path
from .views import (
DashboardView,
get_data,
)

app_name = 'dashboard'

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('get/data', get_data, name='get_data'),
]
