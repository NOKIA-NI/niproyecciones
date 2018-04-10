from django.urls import path
from .views import (
ListLlegada,
DetailLlegada,
CreateLlegada,
UpdateLlegada,
DeleteLlegada,
SearchLlegada,
export_llegada,
)

app_name = 'llegadas'

urlpatterns = [
    path('list/llegada/', ListLlegada.as_view(), name='list_llegada'),
    path('detail/llegada/<int:pk>/', DetailLlegada.as_view(), name='detail_llegada'),
    path('create/llegada/', CreateLlegada.as_view(), name='create_llegada'),
    path('update/llegada/<int:pk>/', UpdateLlegada.as_view(), name='update_llegada'),
    path('delete/llegada/<int:pk/', DeleteLlegada.as_view(), name='delete_llegada'),
    path('search/llegada/', SearchLlegada.as_view(), name='search_llegada'),
    path('export/llegada/', export_llegada, name='export_llegada'),
]
