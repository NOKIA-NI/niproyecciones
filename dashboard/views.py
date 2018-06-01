from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from estaciones.models import Estacion
from partes.models import Parte
from impactos.models import Impacto
from hw_actividades.models import HwActividad
from django.utils import timezone
from django.conf import settings

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == settings.VIERNES or WEEKDAY == settings.SABADO or WEEKDAY == settings.DOMINGO:
    WEEK = WEEK + 1
SI = 'Si'
NO = 'No'
ACCESORIOS = 'Accesorios'
MODULOS = 'Modulos'
ANTENAS_Y_OTROS = 'Antenas y Otros'
MODULO_ACCESORIO = 'Modulo-Accesorio'
ANTENA = 'Antena'
MODULO_ACCESORIO_ANTENA = 'Modulo-Accesorio-Antena'
SITIOSLSM55 = '55 sitios LSM'
SITIOSLSM165 = '165 sitios LSM'
SITIOSLSM170 = '170 sitios LSM'
SITIOSLSM531 = '531 sitios LSM'
SITIOSBULK = 'Sitios Bulk'
AIRSCALE167 = 'Airscale 167'
AIRSCALE116 = 'Airscale 116'
AIRSCALE112 = 'Airscale 112'
REEMPLAZOSITIOSLSM170 = 'Reemplazo 170 sitios LSM'
SITIOSSATELITALESLSM36 = '36 sitios Satelitales LSM'
REEMPLAZOSITIOSSATELITALESLSM36 = 'Reemplazo 36 sitios Satelitales LSM'
PARTESSITIOSLSM302 = 'Partes 302 sitios LSM'

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = 'users:home'
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        week = self.request.GET.get('week', WEEK)
        weeks = list(range(14, 53))
        weeks = [week for week in weeks if week >= WEEK]
        accesorios = Parte.objects.filter(grupo_parte=ACCESORIOS)
        modulos = Parte.objects.filter(grupo_parte=MODULOS)
        antenas = Parte.objects.filter(grupo_parte=ANTENAS_Y_OTROS)
        context['week'] = week
        context['weeks'] = weeks
        context['impactos_modulo_accesorio'] = Impacto.objects.filter(w_fc_imp=week, tipo_impacto=MODULO_ACCESORIO, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        context['impactos_antena'] = Impacto.objects.filter(w_fc_imp=week, tipo_impacto=ANTENA, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        context['impactos_modulo_accesorio_antena'] = Impacto.objects.filter(w_fc_imp=week, tipo_impacto=MODULO_ACCESORIO_ANTENA, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        # context['estaciones_fc_imp'] = Estacion.objects.filter(w_fc_imp=week).count()
        context['estaciones_fc_imp'] = HwActividad.objects.filter(estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count()
        context['impactos_fc_imp'] = Impacto.objects.filter(w_fc_imp=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        context['estaciones_impactos_fc_imp'] = HwActividad.objects.filter(estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() - Impacto.objects.filter(w_fc_imp=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        # context['estaciones_fc_sal'] = Estacion.objects.filter(w_fc_sal=week).count()
        context['estaciones_next_week_fc_imp'] = HwActividad.objects.filter(estacion__w_fc_imp=int(week)+1).order_by('estacion_id').distinct('estacion').count()
        # context['impactos_fc_sal'] = Impacto.objects.filter(w_fc_sal=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        context['accesorios'] = accesorios
        context['modulos'] = modulos
        context['antenas'] = antenas
        return context

class TaskView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    login_url = 'users:home'
    template_name = 'dashboard/task.html'
    permission_required = 'is_superuser'


# def get_data(request):
#     impactos_14 = Impacto.objects.filter(w_fc_sal=14)
#     return JsonResponse(serializers.serialize('json', impactos_14), safe=False)

def impactos(request):
    w_fc = request.GET.get('w_fc', 'w_fc_imp')
    weeks = list(range(14, 53))
    labels = [week for week in weeks if week >= WEEK]
    cronograma = [HwActividad.objects.filter(**{'estacion__'+w_fc:week}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_si = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # impactos_no = [Estacion.objects.filter(**{w_fc:week}).count() - Impacto.objects.filter(**{w_fc:week, 'impactado':SI}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_no = [HwActividad.objects.filter(**{'estacion__'+w_fc:week}).order_by('estacion_id').distinct('estacion').count() - Impacto.objects.filter(**{w_fc:week, 'impactado':SI}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    data = {
        'labels': labels,
        'cronograma': cronograma,
        'impactos_si': impactos_si,
        'impactos_no': impactos_no,
    }
    return JsonResponse(data)

def cronograma_bolsas(request):
    w_fc = request.GET.get('w_fc', 'w_fc_imp')
    weeks = list(range(14, 53))
    labels = [week for week in weeks if week >= WEEK]
    sitioslsm55 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSLSM55}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    sitioslsm165 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSLSM165}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    sitioslsm170 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSLSM170}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    sitioslsm531 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSLSM531}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    sitiosbulk = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSBULK}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    airscale167 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':AIRSCALE167}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    airscale116 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':AIRSCALE116}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    airscale112 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':AIRSCALE112}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    reemplazositioslsm170 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':REEMPLAZOSITIOSLSM170}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    sitiossatelitaleslsm36 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSSATELITALESLSM36}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    reemplazossitiossatelitaleslsm36 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':REEMPLAZOSITIOSSATELITALESLSM36}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    partessitioslsm302 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':PARTESSITIOSLSM302}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    data = {
        'labels': labels,
        'sitioslsm55': sitioslsm55,
        'sitioslsm165': sitioslsm165,
        'sitioslsm170': sitioslsm170,
        'sitioslsm531': sitioslsm531,
        'sitiosbulk': sitiosbulk,
        'airscale167': airscale167,
        'airscale116': airscale116,
        'airscale112': airscale112,
        'reemplazositioslsm170': reemplazositioslsm170,
        'sitiossatelitaleslsm36': sitiossatelitaleslsm36,
        'reemplazossitiossatelitaleslsm36': reemplazossitiossatelitaleslsm36,
        'partessitioslsm302': partessitioslsm302,
    }
    return JsonResponse(data)

def impactos_grupo_parte(request):
    w_fc = request.GET.get('w_fc', 'w_fc_imp')
    # grupo_parte = request.GET.get('grupo_parte', None)
    weeks = list(range(14, 53))
    labels = [week for week in weeks if week >= WEEK]
    impactos_accesorios = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI, 'grupo_parte':ACCESORIOS}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_modulos = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI, 'grupo_parte':MODULOS}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_antenas = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI, 'grupo_parte':ANTENAS_Y_OTROS}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    data = {
        'labels': labels,
        'impactos_accesorios': impactos_accesorios,
        'impactos_modulos': impactos_modulos,
        'impactos_antenas': impactos_antenas,
    }
    return JsonResponse(data)

def impactos_parte(request):
    parte = request.GET.get('parte', None)
    weeks = list(range(14, 53))
    labels = [week for week in weeks if week >= WEEK]
    impactos_parte_fc_imp = [Impacto.objects.filter(w_fc_imp=week, impactado=SI, parte__parte_nokia=parte).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_parte_fc_sal = [Impacto.objects.filter(w_fc_sal=week, impactado=SI, parte__parte_nokia=parte).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    data = {
        'labels': labels,
        'impactos_parte_fc_imp': impactos_parte_fc_imp,
        'impactos_parte_fc_sal': impactos_parte_fc_sal,
    }
    return JsonResponse(data)
