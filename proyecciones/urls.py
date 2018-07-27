from django.urls import path
from .views import (
ListProyeccion,
DetailProyeccion,
CreateProyeccion,
UpdateProyeccion,
DeleteProyeccion,
SearchProyeccion,
FilterProyeccion,
export_proyeccion,
send_proyeccion,
)

app_name = 'proyecciones'

urlpatterns = [
    path('list/proyeccion/web/', ListProyeccion.as_view(), name='list_proyeccion'),
    path('detail/proyeccion/web/<int:pk>/', DetailProyeccion.as_view(), name='detail_proyeccion'),
    path('create/proyeccion/web/', CreateProyeccion.as_view(), name='create_proyeccion'),
    path('update/proyeccion/web/<int:pk>/', UpdateProyeccion.as_view(), name='update_proyeccion'),
    path('delete/proyeccion/web/<int:pk/', DeleteProyeccion.as_view(), name='delete_proyeccion'),
    path('search/proyeccion/web/', SearchProyeccion.as_view(), name='search_proyeccion_web'),
    path('filter/proyeccion/web/', FilterProyeccion.as_view(), name='filter_proyeccion_web'),
    path('export/proyeccion/web/', export_proyeccion, name='export_proyeccion'),
    path('send/proyeccion/', send_proyeccion, name='send_proyeccion'),
]
