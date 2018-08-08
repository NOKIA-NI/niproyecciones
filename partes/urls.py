from django.urls import path
from .views import (
ListParte,
DetailParte,
CreateParte,
UpdateParte,
DeleteParte,
SearchParte,
FilterParte,
export_parte,

create_hw_parte,
update_hw_parte,
delete_hw_parte,
)

app_name = 'partes'

urlpatterns = [
    path('list/parte/', ListParte.as_view(), name='list_parte'),
    path('detail/parte/<int:pk>/', DetailParte.as_view(), name='detail_parte'),
    path('create/parte/', CreateParte.as_view(), name='create_parte'),
    path('update/parte/<int:pk>/', UpdateParte.as_view(), name='update_parte'),
    path('delete/parte/<int:pk/', DeleteParte.as_view(), name='delete_parte'),
    path('search/parte/', SearchParte.as_view(), name='search_parte'),
    path('filter/parte/', FilterParte.as_view(), name='filter_parte'),
    path('export/parte/', export_parte, name='export_parte'),

    path('create/hw/parte/', create_hw_parte, name='create_hw_parte'),
    path('update/hw/parte/', update_hw_parte, name='update_hw_parte'),
    path('delete/hw/parte/', delete_hw_parte, name='delete_hw_parte'),
]
