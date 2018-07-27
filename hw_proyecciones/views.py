from django.shortcuts import render
from django.http import HttpResponse
from hw_proyecciones.models import HwProyeccion, HwEstacion
from proyecciones.models import Proyeccion
from estaciones.models import Estacion, ProyeccionEstacion
from partes.models import Parte
from hw_actividades.models import HwActividad
from django.db.models import Sum
from django.utils import timezone
import datetime
from django.core.mail import send_mail, EmailMessage
from proyecciones.resources import ProyeccionResource

TODAY = timezone.now().date()
# TODAY = datetime.date.today()
TOMORROW = timezone.now() + datetime.timedelta(1)

SI = 'Si'
ENTRO = 'Entro'
SALIO = 'Salio'

def create_proyeccion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_proyecciones = HwProyeccion.objects.all()
    # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
    proyecciones = Proyeccion.objects.all()

    for hw_proyeccion in hw_proyecciones:
        try:
            proyeccion = Proyeccion.objects.get(id=hw_proyeccion.id)
        except Proyeccion.DoesNotExist:
            try:
                estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                    if parte.parte_nokia == 'AISG_4MTS':
                        parte = Parte.objects.get(parte_nokia='AISG_5MTS')
                    if parte.parte_nokia == 'FPCC':
                        parte = Parte.objects.get(parte_nokia='FPCA')
                    if parte.parte_nokia == 'FPBA':
                        parte = Parte.objects.get(parte_nokia='FPBB')
                    if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERFLEX':
                        parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
                    if parte.parte_nokia == 'J_HR_MA_4MTS_PREMIUM':
                        parte = Parte.objects.get(parte_nokia='J_HR_MA_4MTS_DCLASS')
                    if parte.parte_nokia == 'FMCF':
                        parte = Parte.objects.get(parte_nokia='FMCA')
                    if parte.parte_nokia == 'FYTG':
                        parte = Parte.objects.get(parte_nokia='FUFAY')
                    if parte.parte_nokia == 'FSFC':
                        parte = Parte.objects.get(parte_nokia='FUFAY')
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    id=hw_proyeccion.id,
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
                    if parte.parte_nokia == 'AISG_4MTS':
                        parte = Parte.objects.get(parte_nokia='AISG_5MTS')
                    if parte.parte_nokia == 'FPCC':
                        parte = Parte.objects.get(parte_nokia='FPCA')
                    if parte.parte_nokia == 'FPBA':
                        parte = Parte.objects.get(parte_nokia='FPBB')
                    if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERFLEX':
                        parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
                    if parte.parte_nokia == 'J_HR_MA_4MTS_PREMIUM':
                        parte = Parte.objects.get(parte_nokia='J_HR_MA_4MTS_DCLASS')
                    if parte.parte_nokia == 'FMCF':
                        parte = Parte.objects.get(parte_nokia='FMCA')
                    if parte.parte_nokia == 'FYTG':
                        parte = Parte.objects.get(parte_nokia='FUFAY')
                    if parte.parte_nokia == 'FSFC':
                        parte = Parte.objects.get(parte_nokia='FUFAY')
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    id=hw_proyeccion.id,
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

# def create_proyeccion_one(request):
#     # if request.headers["X-Appengine-Cron"]:
#     hw_proyecciones = HwProyeccion.objects.filter(id__gte=0, id__lt=150000)
#     # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
#     proyecciones = Proyeccion.objects.all()
#
#     for hw_proyeccion in hw_proyecciones:
#         try:
#             proyeccion = Proyeccion.objects.get(id=hw_proyeccion.id)
#         except Proyeccion.DoesNotExist:
#             try:
#                 estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
#                 try:
#                     parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
#                     if parte.parte_nokia == 'AISG_4MTS':
#                         parte = Parte.objects.get(parte_nokia='AISG_5MTS')
#                     if parte.parte_nokia == 'FPCC':
#                         parte = Parte.objects.get(parte_nokia='FPCA')
#                     if parte.parte_nokia == 'FPBA':
#                         parte = Parte.objects.get(parte_nokia='FPBB')
#                     if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERCLASS':
#                         parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
#                     if parte.parte_nokia == 'FMCF':
#                         parte = Parte.objects.get(parte_nokia='FMCA')
#                 except Parte.DoesNotExist:
#                     parte = Parte.objects.create(
#                         parte_nokia=hw_proyeccion.parte,
#                     )
#                 proyeccion = Proyeccion.objects.create(
#                     id=hw_proyeccion.id,
#                     estacion=estacion,
#                     proyecto=hw_proyeccion.proyecto,
#                     escenario=hw_proyeccion.escenario,
#                     banda=hw_proyeccion.banda,
#                     agrupadores=hw_proyeccion.agrupadores,
#                     rfe=hw_proyeccion.rfe,
#                     parte=parte,
#                     estado_proyeccion=hw_proyeccion.estado,
#                     cantidad_estimada=hw_proyeccion.cantidad_estimada,
#                 )
#             except Estacion.DoesNotExist:
#                 estacion = Estacion.objects.create(
#                     site_name=hw_proyeccion.siteName,
#                 )
#                 try:
#                     parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
#                     if parte.parte_nokia == 'AISG_4MTS':
#                         parte = Parte.objects.get(parte_nokia='AISG_5MTS')
#                     if parte.parte_nokia == 'FPCC':
#                         parte = Parte.objects.get(parte_nokia='FPCA')
#                     if parte.parte_nokia == 'FPBA':
#                         parte = Parte.objects.get(parte_nokia='FPBB')
#                     if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERCLASS':
#                         parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
#                     if parte.parte_nokia == 'FMCF':
#                         parte = Parte.objects.get(parte_nokia='FMCA')
#                 except Parte.DoesNotExist:
#                     parte = Parte.objects.create(
#                         parte_nokia=hw_proyeccion.parte,
#                     )
#                 proyeccion = Proyeccion.objects.create(
#                     id=hw_proyeccion.id,
#                     estacion=estacion,
#                     proyecto=hw_proyeccion.proyecto,
#                     escenario=hw_proyeccion.escenario,
#                     banda=hw_proyeccion.banda,
#                     agrupadores=hw_proyeccion.agrupadores,
#                     rfe=hw_proyeccion.rfe,
#                     parte=parte,
#                     estado_proyeccion=hw_proyeccion.estado,
#                     cantidad_estimada=hw_proyeccion.cantidad_estimada,
#                 )
#
#     return HttpResponse(status=204)

# def create_proyeccion_two(request):
#     # if request.headers["X-Appengine-Cron"]:
#     hw_proyecciones = HwProyeccion.objects.filter(id__gte=150000, id__lt=300000)
#     # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
#     proyecciones = Proyeccion.objects.all()
#
#     for hw_proyeccion in hw_proyecciones:
#         try:
#             proyeccion = proyecciones.get(id=hw_proyeccion.id)
#         except Proyeccion.DoesNotExist:
#             try:
#                 estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
#                 try:
#                     parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
#                     if parte.parte_nokia == 'AISG_4MTS':
#                         parte = Parte.objects.get(parte_nokia='AISG_5MTS')
#                     if parte.parte_nokia == 'FPCC':
#                         parte = Parte.objects.get(parte_nokia='FPCA')
#                     if parte.parte_nokia == 'FPBA':
#                         parte = Parte.objects.get(parte_nokia='FPBB')
#                     if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERCLASS':
#                         parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
#                     if parte.parte_nokia == 'FMCF':
#                         parte = Parte.objects.get(parte_nokia='FMCA')
#                 except Parte.DoesNotExist:
#                     parte = Parte.objects.create(
#                         parte_nokia=hw_proyeccion.parte,
#                     )
#                 proyeccion = Proyeccion.objects.create(
#                     id=hw_proyeccion.id,
#                     estacion=estacion,
#                     proyecto=hw_proyeccion.proyecto,
#                     escenario=hw_proyeccion.escenario,
#                     banda=hw_proyeccion.banda,
#                     agrupadores=hw_proyeccion.agrupadores,
#                     rfe=hw_proyeccion.rfe,
#                     parte=parte,
#                     estado_proyeccion=hw_proyeccion.estado,
#                     cantidad_estimada=hw_proyeccion.cantidad_estimada,
#                 )
#             except Estacion.DoesNotExist:
#                 estacion = Estacion.objects.create(
#                     site_name=hw_proyeccion.siteName,
#                 )
#                 try:
#                     parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
#                     if parte.parte_nokia == 'AISG_4MTS':
#                         parte = Parte.objects.get(parte_nokia='AISG_5MTS')
#                     if parte.parte_nokia == 'FPCC':
#                         parte = Parte.objects.get(parte_nokia='FPCA')
#                     if parte.parte_nokia == 'FPBA':
#                         parte = Parte.objects.get(parte_nokia='FPBB')
#                     if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERCLASS':
#                         parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
#                     if parte.parte_nokia == 'FMCF':
#                         parte = Parte.objects.get(parte_nokia='FMCA')
#                 except Parte.DoesNotExist:
#                     parte = Parte.objects.create(
#                         parte_nokia=hw_proyeccion.parte,
#                     )
#                 proyeccion = Proyeccion.objects.create(
#                     id=hw_proyeccion.id,
#                     estacion=estacion,
#                     proyecto=hw_proyeccion.proyecto,
#                     escenario=hw_proyeccion.escenario,
#                     banda=hw_proyeccion.banda,
#                     agrupadores=hw_proyeccion.agrupadores,
#                     rfe=hw_proyeccion.rfe,
#                     parte=parte,
#                     estado_proyeccion=hw_proyeccion.estado,
#                     cantidad_estimada=hw_proyeccion.cantidad_estimada,
#                 )
#
#     return HttpResponse(status=204)

# def create_proyeccion_three(request):
#     # if request.headers["X-Appengine-Cron"]:
#     hw_proyecciones = HwProyeccion.objects.filter(id__gte=300000, id__lt=400000)
#     # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
#     proyecciones = Proyeccion.objects.all()
#
#     for hw_proyeccion in hw_proyecciones:
#         try:
#             proyeccion = proyecciones.get(id=hw_proyeccion.id)
#         except Proyeccion.DoesNotExist:
#             try:
#                 estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
#                 try:
#                     parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
#                     if parte.parte_nokia == 'AISG_4MTS':
#                         parte = Parte.objects.get(parte_nokia='AISG_5MTS')
#                     if parte.parte_nokia == 'FPCC':
#                         parte = Parte.objects.get(parte_nokia='FPCA')
#                     if parte.parte_nokia == 'FPBA':
#                         parte = Parte.objects.get(parte_nokia='FPBB')
#                     if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERCLASS':
#                         parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
#                     if parte.parte_nokia == 'FMCF':
#                         parte = Parte.objects.get(parte_nokia='FMCA')
#                 except Parte.DoesNotExist:
#                     parte = Parte.objects.create(
#                         parte_nokia=hw_proyeccion.parte,
#                     )
#                 proyeccion = Proyeccion.objects.create(
#                     id=hw_proyeccion.id,
#                     estacion=estacion,
#                     proyecto=hw_proyeccion.proyecto,
#                     escenario=hw_proyeccion.escenario,
#                     banda=hw_proyeccion.banda,
#                     agrupadores=hw_proyeccion.agrupadores,
#                     rfe=hw_proyeccion.rfe,
#                     parte=parte,
#                     estado_proyeccion=hw_proyeccion.estado,
#                     cantidad_estimada=hw_proyeccion.cantidad_estimada,
#                 )
#             except Estacion.DoesNotExist:
#                 estacion = Estacion.objects.create(
#                     site_name=hw_proyeccion.siteName,
#                 )
#                 try:
#                     parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
#                     if parte.parte_nokia == 'AISG_4MTS':
#                         parte = Parte.objects.get(parte_nokia='AISG_5MTS')
#                     if parte.parte_nokia == 'FPCC':
#                         parte = Parte.objects.get(parte_nokia='FPCA')
#                     if parte.parte_nokia == 'FPBA':
#                         parte = Parte.objects.get(parte_nokia='FPBB')
#                     if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERCLASS':
#                         parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
#                     if parte.parte_nokia == 'FMCF':
#                         parte = Parte.objects.get(parte_nokia='FMCA')
#                 except Parte.DoesNotExist:
#                     parte = Parte.objects.create(
#                         parte_nokia=hw_proyeccion.parte,
#                     )
#                 proyeccion = Proyeccion.objects.create(
#                     id=hw_proyeccion.id,
#                     estacion=estacion,
#                     proyecto=hw_proyeccion.proyecto,
#                     escenario=hw_proyeccion.escenario,
#                     banda=hw_proyeccion.banda,
#                     agrupadores=hw_proyeccion.agrupadores,
#                     rfe=hw_proyeccion.rfe,
#                     parte=parte,
#                     estado_proyeccion=hw_proyeccion.estado,
#                     cantidad_estimada=hw_proyeccion.cantidad_estimada,
#                 )
#
#     return HttpResponse(status=204)

# def create_proyeccion_four(request):
#     # if request.headers["X-Appengine-Cron"]:
#     hw_proyecciones = HwProyeccion.objects.filter(id__gte=400000, id__lt=800000)
#     # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
#     proyecciones = Proyeccion.objects.all()
#
#     for hw_proyeccion in hw_proyecciones:
#         try:
#             proyeccion = proyecciones.get(id=hw_proyeccion.id)
#         except Proyeccion.DoesNotExist:
#             try:
#                 estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
#                 try:
#                     parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
#                     if parte.parte_nokia == 'AISG_4MTS':
#                         parte = Parte.objects.get(parte_nokia='AISG_5MTS')
#                     if parte.parte_nokia == 'FPCC':
#                         parte = Parte.objects.get(parte_nokia='FPCA')
#                     if parte.parte_nokia == 'FPBA':
#                         parte = Parte.objects.get(parte_nokia='FPBB')
#                     if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERCLASS':
#                         parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
#                     if parte.parte_nokia == 'FMCF':
#                         parte = Parte.objects.get(parte_nokia='FMCA')
#                 except Parte.DoesNotExist:
#                     parte = Parte.objects.create(
#                         parte_nokia=hw_proyeccion.parte,
#                     )
#                 proyeccion = Proyeccion.objects.create(
#                     id=hw_proyeccion.id,
#                     estacion=estacion,
#                     proyecto=hw_proyeccion.proyecto,
#                     escenario=hw_proyeccion.escenario,
#                     banda=hw_proyeccion.banda,
#                     agrupadores=hw_proyeccion.agrupadores,
#                     rfe=hw_proyeccion.rfe,
#                     parte=parte,
#                     estado_proyeccion=hw_proyeccion.estado,
#                     cantidad_estimada=hw_proyeccion.cantidad_estimada,
#                 )
#             except Estacion.DoesNotExist:
#                 estacion = Estacion.objects.create(
#                     site_name=hw_proyeccion.siteName,
#                 )
#                 try:
#                     parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
#                     if parte.parte_nokia == 'AISG_4MTS':
#                         parte = Parte.objects.get(parte_nokia='AISG_5MTS')
#                     if parte.parte_nokia == 'FPCC':
#                         parte = Parte.objects.get(parte_nokia='FPCA')
#                     if parte.parte_nokia == 'FPBA':
#                         parte = Parte.objects.get(parte_nokia='FPBB')
#                     if parte.parte_nokia == 'J_MR_MA_8MTS_SUPERCLASS':
#                         parte = Parte.objects.get(parte_nokia='J_MR_MA_8MTS_DCLASS')
#                     if parte.parte_nokia == 'FMCF':
#                         parte = Parte.objects.get(parte_nokia='FMCA')
#                 except Parte.DoesNotExist:
#                     parte = Parte.objects.create(
#                         parte_nokia=hw_proyeccion.parte,
#                     )
#                 proyeccion = Proyeccion.objects.create(
#                     id=hw_proyeccion.id,
#                     estacion=estacion,
#                     proyecto=hw_proyeccion.proyecto,
#                     escenario=hw_proyeccion.escenario,
#                     banda=hw_proyeccion.banda,
#                     agrupadores=hw_proyeccion.agrupadores,
#                     rfe=hw_proyeccion.rfe,
#                     parte=parte,
#                     estado_proyeccion=hw_proyeccion.estado,
#                     cantidad_estimada=hw_proyeccion.cantidad_estimada,
#                 )
#
#     return HttpResponse(status=204)

def update_proyeccion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_proyecciones = HwProyeccion.objects.all()
    # hw_proyecciones = HwProyeccion.objects.filter(lastUpdated__gte=TODAY, lastUpdated__lt=TOMORROW)
    proyecciones = Proyeccion.objects.all()
    for hw_proyeccion in hw_proyecciones:
        try:
            proyeccion = proyecciones.get(id=hw_proyeccion.id)
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
            try:
                estacion = Estacion.objects.get(site_name__iexact=hw_proyeccion.siteName)
                try:
                    parte = Parte.objects.get(parte_nokia__iexact=hw_proyeccion.parte)
                except Parte.DoesNotExist:
                    parte = Parte.objects.create(
                        parte_nokia=hw_proyeccion.parte,
                    )
                proyeccion = Proyeccion.objects.create(
                    id=hw_proyeccion.id,
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
                    id=hw_proyeccion.id,
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

# def delete_proyeccion(request):
#     # if request.headers["X-Appengine-Cron"]:
#     Proyeccion.objects.all().delete()
#
#     return HttpResponse(status=204)

def delete_proyeccion(request):
    proyecciones = Proyeccion.objects.all()
    hw_proyecciones = HwProyeccion.objects.all()

    list_proyecciones = []
    list_hw_proyecciones = []

    for proyeccion in proyecciones:
        list_proyecciones.append(proyeccion.id)

    for hw_proyeccion in hw_proyecciones:
        list_hw_proyecciones.append(hw_proyeccion.id)

    for id in list_proyecciones:
        if id in list_hw_proyecciones:
            pass
        else:
            try:
                Proyeccion.objects.get(id=id).delete()
            except Proyeccion.DoesNotExist:
                pass

    return HttpResponse(status=204)

# def delete_proyeccion(request):
#     # if request.headers["X-Appengine-Cron"]:
#     proyecciones = Proyeccion.objects.all()
#     hw_proyecciones = HwProyeccion.objects.all()
#     for proyeccion in proyecciones:
#         try:
#             hw_proyeccion = HwProyeccion.objects.get(id=proyeccion.hw_proyeccion)
#         except HwProyeccion.DoesNotExist:
#             proyeccion.delete()
#
#     return HttpResponse(status=204)

# def delete_proyeccion(request):
#     # if request.headers["X-Appengine-Cron"]:
#     hw_proyecciones = HwProyeccion.objects.all()
#     proyecciones = Proyeccion.objects.all()
#
#     for hw_proyeccion in hw_proyecciones:
#             proyecciones = proyecciones.exclude(id=hw_proyeccion.id)
#     proyecciones.delete()
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
                ciudad=hw_estacion.ciudad,
                scope_claro=hw_estacion.scope_claro,
                w_fc_imp=hw_estacion.w_fc_c,
                w_fc_c=hw_estacion.w_fc_c,
                total_actividades=hw_estacion.actividades,
                bolsa=hw_estacion.bolsa,
                status_nokia=hw_estacion.status_nokia,
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
                estacion.ciudad != hw_estacion.ciudad or \
                estacion.scope_claro != hw_estacion.scope_claro or \
                estacion.w_fc_imp != hw_estacion.w_fc_c or \
                estacion.w_fc_c != hw_estacion.w_fc_c or \
                estacion.total_actividades != hw_estacion.actividades or \
                estacion.bolsa != hw_estacion.bolsa or \
                estacion.status_nokia != hw_estacion.status_nokia:

                estacion.site_name = hw_estacion.siteName
                estacion.region = hw_estacion.region
                estacion.ciudad = hw_estacion.ciudad
                estacion.scope_claro = hw_estacion.scope_claro
                estacion.w_fc_imp = hw_estacion.w_fc_c
                estacion.w_fc_c = hw_estacion.w_fc_c
                estacion.total_actividades = hw_estacion.actividades
                estacion.bolsa = hw_estacion.bolsa
                estacion.status_nokia = hw_estacion.status_nokia
                estacion.save()
                # estacion.w_fc_imp != hw_estacion.w_proyeccion_instalacion or \
                # estacion.w_fc_imp = hw_estacion.w_proyeccion_instalacion

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

def update_hw_actividad(request):
    hw_actividades = HwActividad.objects.all()

    for hw_actividad in hw_actividades:
        hw_actividad.save()

    return HttpResponse(status=204)

def calculate_consumo_nokia(request):
    partes = Parte.objects.all()

    for parte in partes:
        consumo_w14 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=14, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w15 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=15, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w16 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=16, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w17 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=17, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w18 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=18, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w19 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=19, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w20 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=20, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w21 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=21, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w22 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=22, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w23 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=23, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w24 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=24, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w25 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=25, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w26 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=26, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w27 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=27, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w28 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=28, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w29 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=29, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w30 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=30, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w31 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=31, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w32 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=32, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w33 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=33, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w34 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=34, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w35 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=35, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w36 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=36, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w37 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=37, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w38 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=38, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w39 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=39, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w40 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=40, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w41 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=41, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w42 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=42, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w43 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=43, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w44 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=44, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w45 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=45, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w46 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=46, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w47 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=47, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w48 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=48, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w49 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=49, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w50 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=50, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w51 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=51, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w52 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=52, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')

        if consumo_w14 is not None:
            parte.consumonokia.w14 = consumo_w14
        else:
            parte.consumonokia.w14 = 0
        if consumo_w15 is not None:
            parte.consumonokia.w15 = consumo_w15
        else:
            parte.consumonokia.w15 = 0
        if consumo_w16 is not None:
            parte.consumonokia.w16 = consumo_w16
        else:
            parte.consumonokia.w16 = 0
        if consumo_w17 is not None:
            parte.consumonokia.w17 = consumo_w17
        else:
            parte.consumonokia.w17 = 0
        if consumo_w18 is not None:
            parte.consumonokia.w18 = consumo_w18
        else:
            parte.consumonokia.w18 = 0
        if consumo_w19 is not None:
            parte.consumonokia.w19 = consumo_w19
        else:
            parte.consumonokia.w19 = 0
        if consumo_w20 is not None:
            parte.consumonokia.w20 = consumo_w20
        else:
            parte.consumonokia.w20 = 0
        if consumo_w21 is not None:
            parte.consumonokia.w21 = consumo_w21
        else:
            parte.consumonokia.w21 = 0
        if consumo_w22 is not None:
            parte.consumonokia.w22 = consumo_w22
        else:
            parte.consumonokia.w22 = 0
        if consumo_w23 is not None:
            parte.consumonokia.w23 = consumo_w23
        else:
            parte.consumonokia.w23 = 0
        if consumo_w24 is not None:
            parte.consumonokia.w24 = consumo_w24
        else:
            parte.consumonokia.w24 = 0
        if consumo_w25 is not None:
            parte.consumonokia.w25 = consumo_w25
        else:
            parte.consumonokia.w25 = 0
        if consumo_w26 is not None:
            parte.consumonokia.w26 = consumo_w26
        else:
            parte.consumonokia.w26 = 0
        if consumo_w27 is not None:
            parte.consumonokia.w27 = consumo_w27
        else:
            parte.consumonokia.w27 = 0
        if consumo_w28 is not None:
            parte.consumonokia.w28 = consumo_w28
        else:
            parte.consumonokia.w28 = 0
        if consumo_w29 is not None:
            parte.consumonokia.w29 = consumo_w29
        else:
            parte.consumonokia.w29 = 0
        if consumo_w30 is not None:
            parte.consumonokia.w30 = consumo_w30
        else:
            parte.consumonokia.w30 = 0
        if consumo_w31 is not None:
            parte.consumonokia.w31 = consumo_w31
        else:
            parte.consumonokia.w31 = 0
        if consumo_w32 is not None:
            parte.consumonokia.w32 = consumo_w32
        else:
            parte.consumonokia.w32 = 0
        if consumo_w33 is not None:
            parte.consumonokia.w33 = consumo_w33
        else:
            parte.consumonokia.w33 = 0
        if consumo_w34 is not None:
            parte.consumonokia.w34 = consumo_w34
        else:
            parte.consumonokia.w34 = 0
        if consumo_w35 is not None:
            parte.consumonokia.w35 = consumo_w35
        else:
            parte.consumonokia.w35 = 0
        if consumo_w36 is not None:
            parte.consumonokia.w36 = consumo_w36
        else:
            parte.consumonokia.w36 = 0
        if consumo_w37 is not None:
            parte.consumonokia.w37 = consumo_w37
        else:
            parte.consumonokia.w37 = 0
        if consumo_w38 is not None:
            parte.consumonokia.w38 = consumo_w38
        else:
            parte.consumonokia.w38 = 0
        if consumo_w39 is not None:
            parte.consumonokia.w39 = consumo_w39
        else:
            parte.consumonokia.w39 = 0
        if consumo_w40 is not None:
            parte.consumonokia.w40 = consumo_w40
        else:
            parte.consumonokia.w40 = 0
        if consumo_w41 is not None:
            parte.consumonokia.w41 = consumo_w41
        else:
            parte.consumonokia.w41 = 0
        if consumo_w42 is not None:
            parte.consumonokia.w42 = consumo_w42
        else:
            parte.consumonokia.w42 = 0
        if consumo_w43 is not None:
            parte.consumonokia.w43 = consumo_w43
        else:
            parte.consumonokia.w43 = 0
        if consumo_w44 is not None:
            parte.consumonokia.w44 = consumo_w44
        else:
            parte.consumonokia.w44 = 0
        if consumo_w45 is not None:
            parte.consumonokia.w45 = consumo_w45
        else:
            parte.consumonokia.w45 = 0
        if consumo_w46 is not None:
            parte.consumonokia.w46 = consumo_w46
        else:
            parte.consumonokia.w46 = 0
        if consumo_w47 is not None:
            parte.consumonokia.w47 = consumo_w47
        else:
            parte.consumonokia.w47 = 0
        if consumo_w48 is not None:
            parte.consumonokia.w48 = consumo_w48
        else:
            parte.consumonokia.w48 = 0
        if consumo_w49 is not None:
            parte.consumonokia.w49 = consumo_w49
        else:
            parte.consumonokia.w49 = 0
        if consumo_w50 is not None:
            parte.consumonokia.w50 = consumo_w50
        else:
            parte.consumonokia.w50 = 0
        if consumo_w51 is not None:
            parte.consumonokia.w51 = consumo_w51
        else:
            parte.consumonokia.w51 = 0
        if consumo_w52 is not None:
            parte.consumonokia.w52 = consumo_w52
        else:
            parte.consumonokia.w52 = 0

        parte.consumonokia.save()

    return HttpResponse(status=204)

def create_proyeccion_estacion_entro(request):
    # if request.headers["X-Appengine-Cron"]:
    proyeciones = Proyeccion.objects.all().order_by('estacion_id').distinct('estacion')
    proyeciones_estacion = ProyeccionEstacion.objects.all()
    pk_list = []

    for proyecion in proyeciones:
        try:
            proyeccion_estacion = ProyeccionEstacion.objects.get(estacion=proyecion.estacion)
        except ProyeccionEstacion.DoesNotExist:
            proyeccion_estacion = ProyeccionEstacion.objects.create(
                estacion=proyecion.estacion,
                proyeccion=ENTRO
            )
            pk_list.append(proyeccion_estacion.estacion.pk)

    estaciones = Estacion.objects.filter(pk__in=pk_list)
    data = [estacion.site_name for estacion in estaciones]
    data = ', '.join(data)
    send_mail(
        'Entrada de Sitios a la Proyeccion de Hardware',
        'Sitios que Entraron a la Proyeccion de Hardware el '+ proyeccion_estacion.fecha_proyeccion.strftime('%Y-%m-%d') +'\n'+'\n'+ \
        data,
        'notificaciones@nihardware.com',
        [
        'jbri.gap@nokia.com',
        'hw.proyections@nokia.com',
        'administration.hw@nokia.com',
        'hw_control_2.ni@nokia.com',
        'csp_support.ni_co@nokia.com',
        ],
        fail_silently=False,
    )

    return HttpResponse(status=204)

def create_proyeccion_estacion_salio(request):
    # if request.headers["X-Appengine-Cron"]:
    proyeciones_estacion = ProyeccionEstacion.objects.all()
    proyeciones = Proyeccion.objects.all().order_by('estacion_id').distinct('estacion')
    pk_list = []

    for proyecion_estacion in proyeciones_estacion:
        try:
            proyeccion = proyeciones.get(estacion=proyecion_estacion.estacion)
        except Proyeccion.DoesNotExist:
            proyeccion_estacion = ProyeccionEstacion.objects.create(
                estacion=proyecion_estacion.estacion,
                proyeccion=SALIO
            )
            pk_list.append(proyeccion_estacion.estacion.pk)
    
    estaciones = Estacion.objects.filter(pk__in=pk_list)
    data = [estacion.site_name for estacion in estaciones]
    data = ', '.join(data)
    send_mail(
        'Salida de Sitios de la Proyeccion de Hardware',
        'Sitios que Salieron de la Proyeccion de Hardware el '+ proyeccion_estacion.fecha_proyeccion.strftime('%Y-%m-%d') +'\n'+'\n'+ \
        data,
        'notificaciones@nihardware.com',
        [
        'jbri.gap@nokia.com',
        'hw.proyections@nokia.com',
        'administration.hw@nokia.com',
        'hw_control_2.ni@nokia.com',
        'csp_support.ni_co@nokia.com',
        ],
        fail_silently=False,
    )

    return HttpResponse(status=204)

def send_mail_proyeccion(request):
    # if request.headers["X-Appengine-Cron"]:
    proyeccion_resource = ProyeccionResource()
    proyeccion = proyeccion_resource.export()
    filename = 'Proyeccion-' + TODAY.strftime('%Y-%m-%d') + '.xlsx'
    content = proyeccion.xlsx
    mimetype = 'application/vnd.ms-excel'
    message = EmailMessage(
        'Proyecciones de Hardware',
        'Proyecciones de Hardware ' + TODAY.strftime('%Y-%m-%d'),
        'notificaciones@nihardware.com',
        [
        'jbri.gap@nokia.com',
        'hw.proyections@nokia.com',
        'administration.hw@nokia.com',
        'hw_control_2.ni@nokia.com',
        'hw_control.ni@nokia.com',
        'csp_support.ni_co@nokia.com',
        'camilo.lozano@nokia.com',
        ],
        )
    message.attach(filename, content, mimetype)
    message.send(fail_silently=False)

    return HttpResponse(status=204)
