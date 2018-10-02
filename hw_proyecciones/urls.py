from django.urls import path
from .views import (
# ListHwProyeccion,
# SearchHwProyeccion,
# export_hw_proyeccion
create_proyeccion,
# create_proyeccion_one,
# create_proyeccion_two,
# create_proyeccion_three,
# create_proyeccion_four,
update_proyeccion,
delete_proyeccion,

update_hw_actividad,
calculate_consumo_nokia,

create_proyeccion_estacion_entro,
create_proyeccion_estacion_salio,

send_mail_proyeccion,

save_drill_down,
)

app_name = 'hw_proyecciones'

urlpatterns = [
    # path('list/hw/proyeccion/', ListHwProyeccion.as_view(), name='list_hw_proyeccion'),
    # path('search/hw/proyeccion/', SearchHwProyeccion.as_view(), name='search_hw_proyeccion'),
    # path('export/hw/proyeccion/', export_hw_proyeccion, name='export_hw_proyeccion'),
    path('create/hw/proyeccion/', create_proyeccion, name='create_hw_proyeccion'),
    # path('create/hw/proyeccion/one/', create_proyeccion_one, name='create_hw_proyeccion_one'),
    # path('create/hw/proyeccion/two/', create_proyeccion_two, name='create_hw_proyeccion_two'),
    # path('create/hw/proyeccion/three/', create_proyeccion_three, name='create_hw_proyeccion_three'),
    # path('create/hw/proyeccion/four/', create_proyeccion_four, name='create_hw_proyeccion_four'),
    path('update/hw/proyeccion/', update_proyeccion, name='update_hw_proyeccion'),
    path('delete/hw/proyeccion/', delete_proyeccion, name='delete_hw_proyeccion'),

    path('update/hw/actividad/', update_hw_actividad, name='update_hw_actividad'),
    path('calculate/consumo/nokia/', calculate_consumo_nokia, name='calculate_consumo_nokia'),

    path('create/proyeccion/estacion/entro/', create_proyeccion_estacion_entro, name='create_proyeccion_estacion_entro'),
    path('create/proyeccion/estacion/salio/', create_proyeccion_estacion_salio, name='create_proyeccion_estacion_salio'),

    path('send/mail/proyeccion/', send_mail_proyeccion, name='send_mail_proyeccion'),

    path('save/drill/down/', save_drill_down, name='save_drill_down'),
]