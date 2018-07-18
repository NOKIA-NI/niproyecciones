from django.urls import path
from .views import (
ListTarea,
DetailTarea,
# CreateTarea,
# UpdateTarea,
# DeleteTarea,

get_task_status,
)

app_name = 'tareas'

urlpatterns = [
    path('list/tarea/', ListTarea.as_view(), name='list_tarea'),
    path('detail/tarea/<int:pk>/', DetailTarea.as_view(), name='detail_tarea'),
    # path('create/tarea/', CreateTarea.as_view(), name='create_tarea'),
    # path('update/tarea/<int:pk>/', UpdateTarea.as_view(), name='update_tarea'),
    # path('delete/tarea/<int:pk>/', DeleteTarea.as_view(), name='delete_tarea'),

    path('get/task/status/', get_task_status, name='get_task_status'),
]
