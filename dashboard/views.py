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
ANTENAS = 'Antenas'
MODULO_ACCESORIO = 'Modulo-Accesorio'
ANTENA = 'Antena'
MODULO_ACCESORIO_ANTENA = 'Modulo-Accesorio-Antena'
SITIOSLSM55 = '55 sitios LSM'
SITIOSLSM165 = '165 sitios LSM'
SITIOSLSM170 = '170 sitios LSM'
SITIOSLSM531 = '531 sitios LSM'
SITIOSBULK = 'Sitios Bulk'
AIRSCALE167 = 'Airscale 167'
SITIOSLSMMIXTO381 = '381 sitios LSM Mixto (Airscale + FSMF)'
SITIOSLSMMIXTO114 = '114 sitios LSM Mixto (Airscale + FSMF)'
SITIOSLSMMIXTO78 = '78 sitios LSM Mixto (Airscale + FSMF)'
REEMPLAZOSITIOSLSM170 = 'Reemplazo 170 sitios LSM'
SITIOSSATELITALESLSM36 = '36 sitios Satelitales LSM'
REEMPLAZOSITIOSSATELITALESLSM36 = 'Reemplazo 36 sitios Satelitales LSM'
PARTESSITIOSLSM302 = 'Partes 302 sitios LSM'
PENDIENTEPEDIDO = 'Pendiente Pedido'

CUSTOM_CLEARANCE = 'Custom Clearance'
COMPLETE_SITES = 'Complete Sites (Installed)'
WAITING_CSP_CONFIGURATION = 'Waiting CSP Configuration'
PENDING_PROJECT_HW_REQUEST = 'Pending Project HW Request'
TO_DISPATCH = 'To Dispatch'
WAITING_FACTORY_FEEDBACK = 'Waiting Factory Feedback'

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
        antenas = Parte.objects.filter(grupo_parte=ANTENAS)
        context['week'] = week
        context['weeks'] = weeks
        context['impactos_antena'] = Impacto.objects.filter(w_fc_imp=week, tipo_impacto=ANTENA, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        context['impactos_modulo_accesorio'] = Impacto.objects.filter(w_fc_imp=week, tipo_impacto=MODULO_ACCESORIO, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        context['impactos_modulo_accesorio_antena'] = Impacto.objects.filter(w_fc_imp=week, tipo_impacto=MODULO_ACCESORIO_ANTENA, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        # context['estaciones_fc_imp'] = HwActividad.objects.filter(estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count()

        if week != WEEK:
            context['estaciones_fc_imp'] = Estacion.objects.filter(w_fc_imp=week).count()
            context['impactos_fc_imp'] = Impacto.objects.filter(w_fc_imp=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
            # context['estaciones_impactos_fc_imp'] = HwActividad.objects.filter(estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() - Impacto.objects.filter(w_fc_imp=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
            context['estaciones_impactos_fc_imp'] = Estacion.objects.filter(w_fc_imp=week).count() - Impacto.objects.filter(w_fc_imp=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        else:
            context['estaciones_fc_imp'] = Estacion.objects.filter(w_fc_imp__gte=0).count()
            context['impactos_fc_imp'] = Impacto.objects.filter(w_fc_imp__gte=0, impactado=SI).order_by('estacion_id').distinct('estacion').count()
            # context['estaciones_impactos_fc_imp'] = HwActividad.objects.filter(estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() - Impacto.objects.filter(w_fc_imp=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
            context['estaciones_impactos_fc_imp'] = Estacion.objects.filter(w_fc_imp__gte=0).count() - Impacto.objects.filter(w_fc_imp__gte=0, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        
        # context['estaciones_fc_sal'] = Estacion.objects.filter(w_fc_sal=week).count()
        # context['estaciones_next_week_fc_imp'] = HwActividad.objects.filter(estacion__w_fc_imp=int(week)+1).order_by('estacion_id').distinct('estacion').count()
        context['estaciones_next_week_fc_imp'] = Estacion.objects.filter(w_fc_imp=int(week)+1).count()
        # context['impactos_fc_sal'] = Impacto.objects.filter(w_fc_sal=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        context['accesorios'] = accesorios
        context['modulos'] = modulos
        context['antenas'] = antenas
        return context

# def get_data(request):
#     impactos_14 = Impacto.objects.filter(w_fc_sal=14)
#     return JsonResponse(serializers.serialize('json', impactos_14), safe=False)

def impactos(request):
    w_fc = request.GET.get('w_fc', 'w_fc_imp')
    weeks = list(range(14, 53))
    labels = [week for week in weeks if week >= WEEK]
    # cronograma = [HwActividad.objects.filter(**{'estacion__'+w_fc:week}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    cronograma = [Estacion.objects.filter(**{w_fc:week}).count() for week in weeks if int(week) >= WEEK]
    impactos_si = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_antena = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI, 'tipo_impacto':ANTENA}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_modulo_accesorio = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI, 'tipo_impacto':MODULO_ACCESORIO}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_modulo_accesorio_antena = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI, 'tipo_impacto':MODULO_ACCESORIO_ANTENA}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # impactos_no = [HwActividad.objects.filter(**{'estacion__'+w_fc:week}).order_by('estacion_id').distinct('estacion').count() - Impacto.objects.filter(**{w_fc:week, 'impactado':SI}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_no = [Estacion.objects.filter(**{w_fc:week}).count() - Impacto.objects.filter(**{w_fc:week, 'impactado':SI}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    data = {
        'labels': labels,
        'cronograma': cronograma,
        'impactos_si': impactos_si,
        'impactos_antena': impactos_antena,
        'impactos_modulo_accesorio': impactos_modulo_accesorio,
        'impactos_modulo_accesorio_antena': impactos_modulo_accesorio_antena,
        'impactos_no': impactos_no,
    }
    return JsonResponse(data)

def cronograma_bolsas(request):
    w_fc = request.GET.get('w_fc', 'w_fc_imp')
    weeks = list(range(14, 53))
    labels = [week for week in weeks if week >= WEEK]
    # sitioslsm55 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSLSM55}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # sitioslsm165 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSLSM165}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # sitioslsm170 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSLSM170}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # sitioslsm531 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSLSM531}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # sitiosbulk = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSBULK}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # airscale167 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':AIRSCALE167}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # sitioslsmmixto381 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSLSMMIXTO381}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # reemplazositioslsm170 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':REEMPLAZOSITIOSLSM170}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # sitiossatelitaleslsm36 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':SITIOSSATELITALESLSM36}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # reemplazossitiossatelitaleslsm36 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':REEMPLAZOSITIOSSATELITALESLSM36}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    # partessitioslsm302 = [HwActividad.objects.filter(**{'estacion__'+w_fc:week, 'estacion__bolsa':PARTESSITIOSLSM302}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]

    sitioslsm55 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':SITIOSLSM55}).count() for week in weeks if int(week) >= WEEK]
    sitioslsm165 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':SITIOSLSM165}).count() for week in weeks if int(week) >= WEEK]
    sitioslsm170 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':SITIOSLSM170}).count() for week in weeks if int(week) >= WEEK]
    sitioslsm531 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':SITIOSLSM531}).count() for week in weeks if int(week) >= WEEK]
    sitiosbulk = [Estacion.objects.filter(**{w_fc:week, 'bolsa':SITIOSBULK}).count() for week in weeks if int(week) >= WEEK]
    airscale167 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':AIRSCALE167}).count() for week in weeks if int(week) >= WEEK]
    sitioslsmmixto381 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':SITIOSLSMMIXTO381}).count() for week in weeks if int(week) >= WEEK]
    sitioslsmmixto114 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':SITIOSLSMMIXTO114}).count() for week in weeks if int(week) >= WEEK]
    sitioslsmmixto78 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':SITIOSLSMMIXTO78}).count() for week in weeks if int(week) >= WEEK]
    reemplazositioslsm170 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':REEMPLAZOSITIOSLSM170}).count() for week in weeks if int(week) >= WEEK]
    sitiossatelitaleslsm36 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':SITIOSSATELITALESLSM36}).count() for week in weeks if int(week) >= WEEK]
    reemplazossitiossatelitaleslsm36 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':REEMPLAZOSITIOSSATELITALESLSM36}).count() for week in weeks if int(week) >= WEEK]
    partessitioslsm302 = [Estacion.objects.filter(**{w_fc:week, 'bolsa':PARTESSITIOSLSM302}).count() for week in weeks if int(week) >= WEEK]
    pendientepedido = [Estacion.objects.filter(**{w_fc:week, 'bolsa':PENDIENTEPEDIDO}).count() for week in weeks if int(week) >= WEEK]

    data = {
        'labels': labels,
        'sitioslsm55': sitioslsm55,
        'sitioslsm165': sitioslsm165,
        'sitioslsm170': sitioslsm170,
        'sitioslsm531': sitioslsm531,
        'sitiosbulk': sitiosbulk,
        'airscale167': airscale167,
        'sitioslsmmixto381': sitioslsmmixto381,
        'sitioslsmmixto114': sitioslsmmixto114,
        'sitioslsmmixto78': sitioslsmmixto78,
        'reemplazositioslsm170': reemplazositioslsm170,
        'sitiossatelitaleslsm36': sitiossatelitaleslsm36,
        'reemplazossitiossatelitaleslsm36': reemplazossitiossatelitaleslsm36,
        'partessitioslsm302': partessitioslsm302,
        'pendientepedido': pendientepedido,
    }
    return JsonResponse(data)

def cronograma_status_nokia(request):
    w_fc = request.GET.get('w_fc', 'w_fc_imp')
    weeks = list(range(14, 53))
    labels = [week for week in weeks if week >= WEEK]

    custom_clearance = [Estacion.objects.filter(**{w_fc:week, 'status_nokia':CUSTOM_CLEARANCE}).count() for week in weeks if int(week) >= WEEK]
    complete_sites = [Estacion.objects.filter(**{w_fc:week, 'status_nokia':COMPLETE_SITES}).count() for week in weeks if int(week) >= WEEK]
    waiting_csp_configuration = [Estacion.objects.filter(**{w_fc:week, 'status_nokia':WAITING_CSP_CONFIGURATION}).count() for week in weeks if int(week) >= WEEK]
    pending_project_hw_request = [Estacion.objects.filter(**{w_fc:week, 'status_nokia':PENDING_PROJECT_HW_REQUEST}).count() for week in weeks if int(week) >= WEEK]
    to_dispatch = [Estacion.objects.filter(**{w_fc:week, 'status_nokia':TO_DISPATCH}).count() for week in weeks if int(week) >= WEEK]
    waiting_factory_feedback = [Estacion.objects.filter(**{w_fc:week, 'status_nokia':WAITING_FACTORY_FEEDBACK}).count() for week in weeks if int(week) >= WEEK]

    data = {
        'labels': labels,
        'custom_clearance': custom_clearance,
        'complete_sites': complete_sites,
        'waiting_csp_configuration': waiting_csp_configuration,
        'pending_project_hw_request': pending_project_hw_request,
        'to_dispatch': to_dispatch,
        'waiting_factory_feedback': waiting_factory_feedback,
    }
    return JsonResponse(data)

def impactos_grupo_parte(request):
    w_fc = request.GET.get('w_fc', 'w_fc_imp')
    # grupo_parte = request.GET.get('grupo_parte', None)
    weeks = list(range(14, 53))
    labels = [week for week in weeks if week >= WEEK]
    impactos_accesorios = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI, 'grupo_parte':ACCESORIOS}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_modulos = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI, 'grupo_parte':MODULOS}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_antenas = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI, 'grupo_parte':ANTENAS}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
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
