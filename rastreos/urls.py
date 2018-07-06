from django.urls import path
from .views import (
ListRastreo,
DetailRastreo,
CreateRastreo,
UpdateRastreo,
DeleteRastreo,
SearchRastreo,
FilterRastreo,

ListPerfilRastreo,
DetailPerfilRastreo,
SearchPerfilRastreo,
FilterPerfilRastreo,
testemail,

ListProceso,
DetailProceso,
CreateProceso,
UpdateProceso,
DeleteProceso,
SearchProceso,
FilterProceso,

ListPerfilProceso,
UpdatePerfilProceso,
SearchPerfilProceso,
FilterPerfilProceso,
)

app_name = 'rastreos'

urlpatterns = [
    path('list/rastreo/', ListRastreo.as_view(), name='list_rastreo'),
    path('detail/rastreo/<int:pk>/', DetailRastreo.as_view(), name='detail_rastreo'),
    path('create/rastreo/', CreateRastreo.as_view(), name='create_rastreo'),
    path('update/rastreo/<int:pk>/', UpdateRastreo.as_view(), name='update_rastreo'),
    path('delete/rastreo/<int:pk>/', DeleteRastreo.as_view(), name='delete_rastreo'),
    path('search/rastreo/', SearchRastreo.as_view(), name='search_rastreo'),
    path('filter/rastreo/', FilterRastreo.as_view(), name='filter_rastreo'),
    path('testemail', testemail, name='testemail'),

    path('list/perfil/rastreo/', ListPerfilRastreo.as_view(), name='list_perfil_rastreo'),
    path('detail/perfil/rastreo/<int:pk>/', DetailPerfilRastreo.as_view(), name='detail_perfil_rastreo'),
    path('search/perfil/rastreo/', SearchPerfilRastreo.as_view(), name='search_perfil_rastreo'),
    path('filter/perfil/rastreo/', FilterPerfilRastreo.as_view(), name='filter_perfil_rastreo'),

    path('list/proceso/', ListProceso.as_view(), name='list_proceso'),
    path('detail/proceso/<int:pk>/', DetailProceso.as_view(), name='detail_proceso'),
    path('create/proceso/', CreateProceso.as_view(), name='create_proceso'),
    path('update/proceso/<int:pk>/', UpdateProceso.as_view(), name='update_proceso'),
    path('delete/proceso/<int:pk>/', DeleteProceso.as_view(), name='delete_rastreo'),
    path('search/proceso/', SearchProceso.as_view(), name='search_proceso'),
    path('filter/proceso/', FilterProceso.as_view(), name='filter_proceso'),

    path('list/perfil/proceso/', ListPerfilProceso.as_view(), name='list_perfil_proceso'),
    path('update/perfil/proceso/<int:pk>/', UpdatePerfilProceso.as_view(), name='update_perfil_proceso'),
    path('search/perfil/proceso/', SearchPerfilProceso.as_view(), name='search_perfil_proceso'),
    path('filter/perfil/proceso/', FilterPerfilProceso.as_view(), name='filter_perfil_proceso'),
]