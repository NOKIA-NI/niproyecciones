from django.urls import path
from .views import (
ListProyeccion,
DetailProyeccion,
UpdateProyeccion,
CreateProyeccion,
DeleteProyeccion,
SearchProyeccion,
export_proyeccion
)

app_name = 'proyecciones'

urlpatterns = [
    path('list/proyeccion/', ListProyeccion.as_view(), name='list_proyeccion'),
    path('detail/proyeccion/<int:pk>/', DetailProyeccion.as_view(), name='detail_proyeccion'),
    path('create/proyeccion/', CreateProyeccion.as_view(), name='create_proyeccion'),
    path('update/proyeccion/<int:pk>/', UpdateProyeccion.as_view(), name='update_proyeccion'),
    path('delete/proyeccion/<int:pk/', DeleteProyeccion.as_view(), name='delete_proyeccion'),
    path('search/proyeccion/', SearchProyeccion.as_view(), name='search_proyeccion'),
    path('export/proyeccion/', export_proyeccion, name='export_proyeccion'),
]
