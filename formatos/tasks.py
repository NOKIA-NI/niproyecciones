from celery import shared_task, current_task
from .models import FormatoEstacion, FormatoParte, FormatoClaro, FormatoClaroTotal, FormatoClaroKit
from django.core.mail import send_mail as _send_mail
from proyecciones.models import Proyeccion
from partes.models import Parte
from django.db.models import Sum, Value as V
from django.db.models.functions import Coalesce

FORMATOABASTECIMIENTO = 'Formato Abastecimiento'

FCOB = 'FCOB'
ASIA = 'ASIA'
AMIA = 'AMIA'
ABIA = 'ABIA'

try:
    PARTE = Parte.objects.get(parte_nokia='AirScale Base Setup Outdoor Rack + Shelf + 1 ASIA + 1 ABIA')
except:
    pass

@shared_task
def task_create_formato_estacion():
    FormatoEstacion.objects.all().delete()
    FormatoClaroTotal.objects.all().delete()
    FormatoClaroKit.objects.all().delete()
    proyecciones = Proyeccion.objects.filter(estacion__bolsa=FORMATOABASTECIMIENTO).order_by('estacion_id').distinct('estacion')
    for proyeccion in proyecciones:
        try:
            formato_estacion = FormatoEstacion.objects.get(estacion=proyeccion.estacion)
        except FormatoEstacion.DoesNotExist:
            formato_estacion = FormatoEstacion.objects.create(
            estacion = proyeccion.estacion,
            )
        current_task.update_state(state='PROGRESS')
    return {'ok':200}

@shared_task
def task_create_formato_parte():
    FormatoParte.objects.all().delete()
    formatos_estacion = FormatoEstacion.objects.all()
    partes = Parte.objects.all()
    for parte in partes:
        for formato_estacion in formatos_estacion:
            proyecciones = Proyeccion.objects.filter(estacion=formato_estacion.estacion, parte=parte)
            cantidad = proyecciones.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
            if cantidad > 0:
                try:
                    formato_parte = FormatoParte.objects.get(formato_estacion=formato_estacion, parte=parte)
                except FormatoParte.DoesNotExist:
                    formato_parte = FormatoParte.objects.create(
                        formato_estacion = formato_estacion,
                        parte = parte,
                        cantidad = cantidad,
                        )
            current_task.update_state(state='PROGRESS')
    return {'ok':200}

@shared_task
def task_create_formato_claro():
    formatos_parte = FormatoParte.objects.all()
    for formato_parte in formatos_parte:
        try:
            formatos_claro = FormatoClaro.objects.get(formato_parte__id=formato_parte.id)
        except FormatoClaro.DoesNotExist:
            formato_claro = FormatoClaro.objects.create(
                formato_parte = formato_parte,
                )
    return {'ok':200}

@shared_task
def task_create_formato_claro_total():
    FormatoClaroTotal.objects.all().delete()
    formatos_parte = FormatoParte.objects.all().order_by('parte_id').distinct('parte')
    for formato_parte in formatos_parte:
        try:
            formatos_claro_total = FormatoClaroTotal.objects.get(parte=formato_parte.parte)
            total = FormatoParte.objects.filter(parte=formato_parte.parte).aggregate(total=Coalesce(Sum('cantidad'), V(0))).get('total')
            formatos_claro_total.total = total
            formatos_claro_total.save()
        except FormatoClaroTotal.DoesNotExist:
            total = FormatoParte.objects.filter(parte=formato_parte.parte).aggregate(total=Coalesce(Sum('cantidad'), V(0))).get('total')
            formato_claro_total = FormatoClaroTotal.objects.create(
                parte = formato_parte.parte,
                total = total,
                )
        current_task.update_state(state='PROGRESS')
    return {'ok':200}

@shared_task
def task_create_formato_claro_kit():
    FormatoClaroKit.objects.all().delete()
    formatos_claro = FormatoClaro.objects.all()
    for formato_claro in formatos_claro:
        if formato_claro.formato_parte.parte.parte_nokia == FCOB or \
            formato_claro.formato_parte.parte.parte_nokia == ASIA or \
            formato_claro.formato_parte.parte.parte_nokia == AMIA or \
            formato_claro.formato_parte.parte.parte_nokia == ABIA:
            formatos_claro_estacion = formatos_claro.filter(sitio=formato_claro.sitio)
            list_formatos = []
            for formato_claro_estacion in formatos_claro_estacion:
                if formatos_claro_estacion.filter(formato_parte__parte__parte_nokia=FCOB).count() > 0 and \
                    formatos_claro_estacion.filter(formato_parte__parte__parte_nokia=ASIA).count() > 0 and \
                    formatos_claro_estacion.filter(formato_parte__parte__parte_nokia=AMIA).count() > 0 and \
                    formatos_claro_estacion.filter(formato_parte__parte__parte_nokia=ABIA).count() > 0:
                    list_formatos.append(formato_claro_estacion.id)
            if formato_claro.id in list_formatos:
                formato_claro_kit = FormatoClaroKit.objects.create(
                sitio = formato_claro.sitio,
                parte = formato_claro.formato_parte.parte,
                sap = formato_claro.sap,
                descripcion = formato_claro.descripcion,
                qty = formato_claro.qty - 1,
                ciudad = formato_claro.ciudad,
                regional = formato_claro.regional,
                semana = formato_claro.semana,
                mes = formato_claro.mes,
                )
                if formato_claro_kit.qty == 0:
                    formato_claro_kit.delete()
                try:
                    formato_claro_kit = FormatoClaroKit.objects.get(sitio=formato_claro.sitio, parte=PARTE)
                except FormatoClaroKit.DoesNotExist:
                    formato_claro_kit = FormatoClaroKit.objects.create(
                    sitio = formato_claro.sitio,
                    parte = PARTE,
                    sap = PARTE.cod_sap,
                    descripcion = PARTE.capex,
                    qty = 1,
                    ciudad = formato_claro.ciudad,
                    regional = formato_claro.regional,
                    semana = formato_claro.semana,
                    mes = formato_claro.mes,
                    )
            else:
                formato_claro_kit = FormatoClaroKit.objects.create(
                sitio = formato_claro.sitio,
                parte = formato_claro.formato_parte.parte,
                sap = formato_claro.sap,
                descripcion = formato_claro.descripcion,
                qty = formato_claro.qty,
                ciudad = formato_claro.ciudad,
                regional = formato_claro.regional,
                semana = formato_claro.semana,
                mes = formato_claro.mes,
                )
        else:
            formato_claro_kit = FormatoClaroKit.objects.create(
            sitio = formato_claro.sitio,
            parte = formato_claro.formato_parte.parte,
            sap = formato_claro.sap,
            descripcion = formato_claro.descripcion,
            qty = formato_claro.qty,
            ciudad = formato_claro.ciudad,
            regional = formato_claro.regional,
            semana = formato_claro.semana,
            mes = formato_claro.mes,
            )
        current_task.update_state(state='PROGRESS')
    return {'ok':200}