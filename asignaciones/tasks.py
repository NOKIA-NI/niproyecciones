from celery import shared_task, current_task
from .models import (
    AsignacionBulk,
    AsignacionAntena,
    EstadoPo,
    PoZina,
    SitioBolsa,
    SitioBulk,
    )
from estaciones.models import Estacion
from partes.models import Parte
from hw_proyecciones.models import HwSiteList, HwControlRfe

@shared_task
def task_sitios_asignacion():
    current_task.update_state(state='PROGRESS')
    SitioBolsa.objects.all().delete()
    SitioBulk.objects.all().delete()
    status_nokia = ['Complete Sites (Installed)', 'Parcial FXCB', 'Parcial Jumpers', 'Complete Sites (Por Armar LSM)']
    sitios_asignacion = HwSiteList.objects.filter(status_nokia__in=status_nokia, solicitud_hw='1', estado_HW='NO CONFIRMADO')
    Bolsa_HW = ['Sitios Bulk', 'LSM A BULK']
    sitios_asignacion_bolsa = sitios_asignacion.exclude(Bolsa_HW=Bolsa_HW)
    sitios_asignacion_bulk = sitios_asignacion.filter(Bolsa_HW__in=Bolsa_HW)

    for sitio_asignacion_bolsa in sitios_asignacion_bolsa:
        sitio_bolsa = SitioBolsa.objects.create(
            estacion=Estacion.objects.get(site_name__iexact=sitio_asignacion_bolsa.siteName)
        )

    for sitio_asignacion_bulk in sitios_asignacion_bulk:
        sitio_bolsa = SitioBulk.objects.create(
            estacion=Estacion.objects.get(site_name__iexact=sitio_asignacion_bulk.siteName)
        )
    return { 'ok':200 }

@shared_task
def task_asignacion_bolsa():
    current_task.update_state(state='PROGRESS')
    return { 'ok':200 }

@shared_task
def task_asignacion_bulk():
    current_task.update_state(state='PROGRESS')
    return { 'ok':200 }

