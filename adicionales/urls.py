from django.urls import path
from .views import (
ListAdicional,
DetailAdicional,
CreateAdicional,
UpdateAdicional,
DeleteAdicional,
SearchAdicional,
FilterAdicional,
export_adicional,
)

app_name = 'adicionales'

urlpatterns = [
    path('list/adicional/', ListAdicional.as_view(), name='list_adicional'),
    path('detail/adicional/<int:pk>/', DetailAdicional.as_view(), name='detail_adicional'),
    path('create/adicional/', CreateAdicional.as_view(), name='create_adicional'),
    path('update/adicional/<int:pk>/', UpdateAdicional.as_view(), name='update_adicional'),
    path('delete/adicional/<int:pk>/', DeleteAdicional.as_view(), name='delete_adicional'),
    path('search/adicional/', SearchAdicional.as_view(), name='search_adicional'),
    path('filter/adicional/', FilterAdicional.as_view(), name='filter_adicional'),
    path('export/adicional/', export_adicional, name='export_adicional'),
]