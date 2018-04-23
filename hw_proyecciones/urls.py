from django.urls import path
from .views import (
# ListHwProyeccion,
# SearchHwProyeccion,
# export_hw_proyeccion
create_proyeccion_one,
create_proyeccion_two,
create_proyeccion_three,
create_proyeccion_four,
update_proyeccion,
delete_proyeccion,

create_estacion,
update_estacion,
delete_estacion,

calculate_consumo_nokia,
)

app_name = 'hw_proyecciones'

urlpatterns = [
    # path('list/hw/proyeccion/', ListHwProyeccion.as_view(), name='list_hw_proyeccion'),
    # path('search/hw/proyeccion/', SearchHwProyeccion.as_view(), name='search_hw_proyeccion'),
    # path('export/hw/proyeccion/', export_hw_proyeccion, name='export_hw_proyeccion'),
    path('create/hw/proyeccion/one/', create_proyeccion_one, name='create_hw_proyeccion_one'),
    path('create/hw/proyeccion/two/', create_proyeccion_two, name='create_hw_proyeccion_two'),
    path('create/hw/proyeccion/three/', create_proyeccion_three, name='create_hw_proyeccion_three'),
    path('create/hw/proyeccion/four/', create_proyeccion_four, name='create_hw_proyeccion_four'),
    path('update/hw/proyeccion/', update_proyeccion, name='update_hw_proyeccion'),
    path('delete/hw/proyeccion/', delete_proyeccion, name='delete_hw_proyeccion'),

    path('create/hw/estacion/', create_estacion, name='create_hw_estacion'),
    path('update/hw/estacion/', update_estacion, name='update_hw_estacion'),
    path('delete/hw/estacion/', delete_estacion, name='delete_hw_estacion'),

    path('calculate/consumo/nokia/', calculate_consumo_nokia, name='calculate_consumo_nokia'),
]
