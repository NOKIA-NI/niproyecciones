from django.urls import path
from .views import (
ListParte,
DetailParte,
UpdateParte,
CreateParte,
DeleteParte,
SearchParte,
export_parte
)

app_name = 'partes'

urlpatterns = [
    path('list/parte/', ListParte.as_view(), name='list_parte'),
    path('detail/parte/<int:pk>/', DetailParte.as_view(), name='detail_parte'),
    path('create/parte/', CreateParte.as_view(), name='create_parte'),
    path('update/parte/<int:pk>/', UpdateParte.as_view(), name='update_parte'),
    path('delete/parte/<int:pk/', DeleteParte.as_view(), name='delete_parte'),
    path('search/parte/', SearchParte.as_view(), name='search_parte'),
    path('export/parte/', export_parte, name='export_parte'),
]
