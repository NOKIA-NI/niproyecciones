from django.shortcuts import render
from django.http import HttpResponse
from hw_proyecciones.models import HwProyeccion
from proyecciones.models import Proyeccion
from estaciones.models import Estacion
from partes.models import Parte
from django.utils import timezone
import datetime

TODAY = timezone.now().date()
# TODAY = datetime.date.today()
TOMORROW = timezone.now() + datetime.timedelta(1)

def create_proyeccion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_proyecciones = HwProyeccion.objects.all()
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
    hw_proyecciones = HwProyeccion.objects.filter(lastUpdated__gte=TODAY, lastUpdated__lt=TOMORROW)
    proyecciones = Proyeccion.objects.all()
    for hw_proyeccion in hw_proyecciones:
        try:
            proyeccion = proyecciones.get(hw_proyeccion=hw_proyeccion.id)
            if proyeccion:
                try:
                    estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
                except Parte.DoesNotExist:
                    estacion = Estacion.objects.create(
                        site_name=hw_proyeccion.siteName,
                    )
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion.estacion = estacion
                proyeccion.proyecto = hw_proyeccion.proyecto
                proyeccion.escenario = hw_proyeccion.escenario
                proyeccion.banda = hw_proyeccion.banda
                proyeccion.agrupadores = hw_proyeccion.agrupadores
                proyeccion.rfe = hw_proyeccion.rfe
                proyeccion.parte = parte
                proyeccion.estado_proyeccion = hw_proyeccion.estado
                proyeccion.cantidad_estimada = hw_proyeccion.cantidad_estimada
                proyeccion.save()

        except Proyeccion.DoesNotExist:
            pass
    return HttpResponse(status=204)

def delete_proyeccion(request):
    # if request.headers["X-Appengine-Cron"]:
    proyecciones = Proyeccion.objects.all()
    hw_proyecciones = HwProyeccion.objects.all()
    for proyeccion in proyecciones:
        try:
            hw_proyeccion = hw_proyecciones.get(id=proyeccion.hw_proyeccion)
            print('found hw_proyeccion', hw_proyeccion)
        except HwProyeccion.DoesNotExist:
            # proyeccion.delete()
            print('delete proyeccion', proyeccion)

    return HttpResponse(status=204)

# def delete_proyeccion(request):
#     # if request.headers["X-Appengine-Cron"]:
#     hw_proyecciones = HwProyeccion.objects.all()
#     proyecciones = Proyeccion.objects.all()
#     list = []
#     for hw_proyeccion in hw_proyecciones:
#         try:
#             proyeccion = Proyeccion.objects.get(hw_proyeccion=hw_proyeccion.id)
#             print(proyeccion)
#         except:
#             list.append(hw_proyeccion.id)
#             print(list)
#
#     return HttpResponse(status=204)
