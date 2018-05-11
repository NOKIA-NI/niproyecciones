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
ListProyeccionExtra,
DetailProyeccionExtra,
CreateProyeccionExtra,
UpdateProyeccionExtra,
DeleteProyeccionExtra,
SearchProyeccionExtra,
FilterProyeccionExtra,
export_proyeccion_extra
)

app_name = 'proyecciones'

urlpatterns = [
    path('list/proyeccion/', ListProyeccion.as_view(), name='list_proyeccion'),
    path('detail/proyeccion/<int:pk>/', DetailProyeccion.as_view(), name='detail_proyeccion'),
    path('create/proyeccion/', CreateProyeccion.as_view(), name='create_proyeccion'),
    path('update/proyeccion/<int:pk>/', UpdateProyeccion.as_view(), name='update_proyeccion'),
    path('delete/proyeccion/<int:pk/', DeleteProyeccion.as_view(), name='delete_proyeccion'),
    path('search/proyeccion/', SearchProyeccion.as_view(), name='search_proyeccion'),
    path('filter/proyeccion/', FilterProyeccion.as_view(), name='filter_proyeccion'),
    path('export/proyeccion/', export_proyeccion, name='export_proyeccion'),

    path('list/proyeccion/extra', ListProyeccionExtra.as_view(), name='list_proyeccion_extra'),
    path('detail/proyeccion/extra/<int:pk>/', DetailProyeccionExtra.as_view(), name='detail_proyeccion_extra'),
    path('create/proyeccion/extra', CreateProyeccionExtra.as_view(), name='create_proyeccion_extra'),
    path('update/proyeccion/extra/<int:pk>/', UpdateProyeccionExtra.as_view(), name='update_proyeccion_extra'),
    path('delete/proyeccion/extra/<int:pk/', DeleteProyeccionExtra.as_view(), name='delete_proyeccion_extra'),
    path('search/proyeccion/extra', SearchProyeccionExtra.as_view(), name='search_proyeccion_extra'),
    path('filter/proyeccion/extra', FilterProyeccionExtra.as_view(), name='filter_proyeccion_extra'),
    path('export/proyeccion/extra', export_proyeccion_extra, name='export_proyeccion_extra'),
]
