from django.shortcuts import render
from django.http import HttpResponse
from hw_proyecciones.models import HwProyeccion, HwEstacion
from proyecciones.models import Proyeccion
from estaciones.models import Estacion
from partes.models import Parte
from django.utils import timezone
import datetime

TODAY = timezone.now().date()
# TODAY = datetime.date.today()
TOMORROW = timezone.now() + datetime.timedelta(1)

def create_proyeccion_one(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_proyecciones = HwProyeccion.objects.filter(id__gte=0, id__lt=150000)
    # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
    proyecciones = Proyeccion.objects.all()

    for hw_proyeccion in hw_proyecciones:
        try:
            proyeccion = proyecciones.get(hw_proyeccion=hw_proyeccion.id)
        except Proyeccion.DoesNotExist:
            try:
                estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    hw_proyeccion=hw_proyeccion.id,
                    estacion=estacion,
                    proyecto=hw_proyeccion.proyecto,
                    escenario=hw_proyeccion.escenario,
                    banda=hw_proyeccion.banda,
                    agrupadores=hw_proyeccion.agrupadores,
                    rfe=hw_proyeccion.rfe,
                    parte=parte,
                    estado_proyeccion=hw_proyeccion.estado,
                    cantidad_estimada=hw_proyeccion.cantidad_estimada,
                )
            except Estacion.DoesNotExist:
                estacion = Estacion.objects.create(
                    site_name=hw_proyeccion.siteName,
                )
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    hw_proyeccion=hw_proyeccion.id,
                    estacion=estacion,
                    proyecto=hw_proyeccion.proyecto,
                    escenario=hw_proyeccion.escenario,
                    banda=hw_proyeccion.banda,
                    agrupadores=hw_proyeccion.agrupadores,
                    rfe=hw_proyeccion.rfe,
                    parte=parte,
                    estado_proyeccion=hw_proyeccion.estado,
                    cantidad_estimada=hw_proyeccion.cantidad_estimada,
                )

    return HttpResponse(status=204)

def create_proyeccion_two(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_proyecciones = HwProyeccion.objects.filter(id__gte=150000, id__lt=300000)
    # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
    proyecciones = Proyeccion.objects.all()

    for hw_proyeccion in hw_proyecciones:
        try:
            proyeccion = proyecciones.get(hw_proyeccion=hw_proyeccion.id)
        except Proyeccion.DoesNotExist:
            try:
                estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    hw_proyeccion=hw_proyeccion.id,
                    estacion=estacion,
                    proyecto=hw_proyeccion.proyecto,
                    escenario=hw_proyeccion.escenario,
                    banda=hw_proyeccion.banda,
                    agrupadores=hw_proyeccion.agrupadores,
                    rfe=hw_proyeccion.rfe,
                    parte=parte,
                    estado_proyeccion=hw_proyeccion.estado,
                    cantidad_estimada=hw_proyeccion.cantidad_estimada,
                )
            except Estacion.DoesNotExist:
                estacion = Estacion.objects.create(
                    site_name=hw_proyeccion.siteName,
                )
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    hw_proyeccion=hw_proyeccion.id,
                    estacion=estacion,
                    proyecto=hw_proyeccion.proyecto,
                    escenario=hw_proyeccion.escenario,
                    banda=hw_proyeccion.banda,
                    agrupadores=hw_proyeccion.agrupadores,
                    rfe=hw_proyeccion.rfe,
                    parte=parte,
                    estado_proyeccion=hw_proyeccion.estado,
                    cantidad_estimada=hw_proyeccion.cantidad_estimada,
                )

    return HttpResponse(status=204)

def create_proyeccion_three(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_proyecciones = HwProyeccion.objects.filter(id__gte=300000, id__lt=400000)
    # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
    proyecciones = Proyeccion.objects.all()

    for hw_proyeccion in hw_proyecciones:
        try:
            proyeccion = proyecciones.get(hw_proyeccion=hw_proyeccion.id)
        except Proyeccion.DoesNotExist:
            try:
                estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    hw_proyeccion=hw_proyeccion.id,
                    estacion=estacion,
                    proyecto=hw_proyeccion.proyecto,
                    escenario=hw_proyeccion.escenario,
                    banda=hw_proyeccion.banda,
                    agrupadores=hw_proyeccion.agrupadores,
                    rfe=hw_proyeccion.rfe,
                    parte=parte,
                    estado_proyeccion=hw_proyeccion.estado,
                    cantidad_estimada=hw_proyeccion.cantidad_estimada,
                )
            except Estacion.DoesNotExist:
                estacion = Estacion.objects.create(
                    site_name=hw_proyeccion.siteName,
                )
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    hw_proyeccion=hw_proyeccion.id,
                    estacion=estacion,
                    proyecto=hw_proyeccion.proyecto,
                    escenario=hw_proyeccion.escenario,
                    banda=hw_proyeccion.banda,
                    agrupadores=hw_proyeccion.agrupadores,
                    rfe=hw_proyeccion.rfe,
                    parte=parte,
                    estado_proyeccion=hw_proyeccion.estado,
                    cantidad_estimada=hw_proyeccion.cantidad_estimada,
                )

    return HttpResponse(status=204)

def create_proyeccion_four(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_proyecciones = HwProyeccion.objects.filter(id__gte=400000, id__lt=800000)
    # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
    proyecciones = Proyeccion.objects.all()

    for hw_proyeccion in hw_proyecciones:
        try:
            proyeccion = proyecciones.get(hw_proyeccion=hw_proyeccion.id)
        except Proyeccion.DoesNotExist:
            try:
                estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    hw_proyeccion=hw_proyeccion.id,
                    estacion=estacion,
                    proyecto=hw_proyeccion.proyecto,
                    escenario=hw_proyeccion.escenario,
                    banda=hw_proyeccion.banda,
                    agrupadores=hw_proyeccion.agrupadores,
                    rfe=hw_proyeccion.rfe,
                    parte=parte,
                    estado_proyeccion=hw_proyeccion.estado,
                    cantidad_estimada=hw_proyeccion.cantidad_estimada,
                )
            except Estacion.DoesNotExist:
                estacion = Estacion.objects.create(
                    site_name=hw_proyeccion.siteName,
                )
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    hw_proyeccion=hw_proyeccion.id,
                    estacion=estacion,
                    proyecto=hw_proyeccion.proyecto,
                    escenario=hw_proyeccion.escenario,
                    banda=hw_proyeccion.banda,
                    agrupadores=hw_proyeccion.agrupadores,
                    rfe=hw_proyeccion.rfe,
                    parte=parte,
                    estado_proyeccion=hw_proyeccion.estado,
                    cantidad_estimada=hw_proyeccion.cantidad_estimada,
                )

    return HttpResponse(status=204)

def update_proyeccion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_proyecciones = HwProyeccion.objects.all()
    # hw_proyecciones = HwProyeccion.objects.filter(lastUpdated__gte=TODAY, lastUpdated__lt=TOMORROW)
    proyecciones = Proyeccion.objects.all()
    for hw_proyeccion in hw_proyecciones:
        try:
            proyeccion = proyecciones.get(hw_proyeccion=hw_proyeccion.id)
            if proyeccion.proyecto != hw_proyeccion.proyecto or \
                proyeccion.escenario != hw_proyeccion.escenario or \
                proyeccion.banda != hw_proyeccion.banda or \
                proyeccion.agrupadores != hw_proyeccion.agrupadores or \
                proyeccion.rfe != hw_proyeccion.rfe or \
                proyeccion.estado_proyeccion != hw_proyeccion.estado or \
                proyeccion.cantidad_estimada != hw_proyeccion.cantidad_estimada:

                proyeccion.proyecto = hw_proyeccion.proyecto
                proyeccion.escenario = hw_proyeccion.escenario
                proyeccion.banda = hw_proyeccion.banda
                proyeccion.agrupadores = hw_proyeccion.agrupadores
                proyeccion.rfe = hw_proyeccion.rfe
                proyeccion.estado_proyeccion = hw_proyeccion.estado
                proyeccion.cantidad_estimada = hw_proyeccion.cantidad_estimada
                proyeccion.save()

        except Proyeccion.DoesNotExist:
            pass
    return HttpResponse(status=204)

def delete_proyeccion(request):
    # if request.headers["X-Appengine-Cron"]:
    Proyeccion.objects.all().delete()

    return HttpResponse(status=204)

# def delete_proyeccion(request):
#     # if request.headers["X-Appengine-Cron"]:
#     proyecciones = Proyeccion.objects.all()
#     hw_proyecciones = HwProyeccion.objects.all()
#     for proyeccion in proyecciones:
#         try:
#             hw_proyeccion = hw_proyecciones.get(id=proyeccion.hw_proyeccion)
#         except HwProyeccion.DoesNotExist:
#             proyeccion.delete()
#
#     return HttpResponse(status=204)


def create_estacion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_estaciones = HwEstacion.objects.all()
    # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
    estaciones = Estacion.objects.all()

    for hw_estacion in hw_estaciones:
        try:
            estacion = estaciones.get(site_name__iexact=hw_estacion.siteName)
        except Estacion.DoesNotExist:
            estacion = Estacion.objects.create(
                site_name=hw_estacion.siteName,
                region=hw_estacion.region,
                scope_claro=hw_estacion.scope_claro,
                w_fc_imp=hw_estacion.w_proyeccion_instalacion,
                total_actividades=hw_estacion.actividades,
            )

    return HttpResponse(status=204)

def update_estacion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_estaciones = HwEstacion.objects.all()
    # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
    estaciones = Estacion.objects.all()

    for hw_estacion in hw_estaciones:
        try:
            estacion = estaciones.get(site_name__iexact=hw_estacion.siteName)
            if estacion.site_name != hw_estacion.siteName or \
                estacion.region != hw_estacion.region or \
                estacion.scope_claro != hw_estacion.scope_claro or \
                estacion.w_fc_imp != hw_estacion.w_proyeccion_instalacion or \
                estacion.total_actividades != hw_estacion.actividades:

                estacion.site_name = hw_estacion.siteName
                estacion.region = hw_estacion.region
                estacion.scope_claro = hw_estacion.scope_claro
                estacion.w_fc_imp = hw_estacion.w_proyeccion_instalacion
                estacion.total_actividades = hw_estacion.actividades
                estacion.save()

        except Estacion.DoesNotExist:
            pass

    return HttpResponse(status=204)

def delete_estacion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_estaciones = HwEstacion.objects.all()
    estaciones = Estacion.objects.all()

    for hw_estacion in hw_estaciones:
        try:
            estaciones = estaciones.exclude(site_name__iexact=hw_estacion.siteName)
        except Estacion.DoesNotExist:
            pass
    estaciones.delete()

    return HttpResponse(status=204)
