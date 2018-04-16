from django.urls import path
from .views import (
# ListHwProyeccion,
# SearchHwProyeccion,
# export_hw_proyeccion
create_proyeccion,
update_proyeccion,
delete_proyeccion,
)

app_name = 'hw_proyecciones'

urlpatterns = [
    # path('list/hw/proyeccion/', ListHwProyeccion.as_view(), name='list_hw_proyeccion'),
    # path('search/hw/proyeccion/', SearchHwProyeccion.as_view(), name='search_hw_proyeccion'),
    # path('export/hw/proyeccion/', export_hw_proyeccion, name='export_hw_proyeccion'),
    path('create/hw/proyeccion/', create_proyeccion, name='create_hw_proyeccion'),
    path('update/hw/proyeccion/', update_proyeccion, name='update_hw_proyeccion'),
    path('delete/hw/proyeccion/', delete_proyeccion, name='delete_hw_proyeccion'),
]
