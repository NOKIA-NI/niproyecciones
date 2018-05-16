from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from estaciones.models import Estacion
from partes.models import Parte
from impactos.models import Impacto
from django.utils import timezone

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == 4 or WEEKDAY == 5 or WEEKDAY == 6:
    WEEK = WEEK + 1
SI = 'Si'
NO = 'No'
ACCESORIOS = 'Accesorios'
MODULOS = 'Modulos'
ANTENAS_Y_OTROS = 'Antenas y Otros'
MODULO_ACCESORIO = 'Modulo-Accesorio'
ANTENA = 'Antena'
MODULO_ACCESORIO_ANTENA = 'Modulo-Accesorio-Antena'

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
        context['estaciones_fc_imp'] = Estacion.objects.filter(w_fc_imp=week).count()
        context['estaciones_fc_sal'] = Estacion.objects.filter(w_fc_sal=week).count()
        context['impactos_fc_imp'] = Impacto.objects.filter(w_fc_imp=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        context['impactos_fc_sal'] = Impacto.objects.filter(w_fc_sal=week, impactado=SI).order_by('estacion_id').distinct('estacion').count()
        context['impactos_modulo_accesorio'] = Impacto.objects.filter(w_fc_imp=week, tipo_impacto=MODULO_ACCESORIO).order_by('estacion_id').distinct('estacion').count()
        context['impactos_antena'] = Impacto.objects.filter(w_fc_imp=week, tipo_impacto=ANTENA).order_by('estacion_id').distinct('estacion').count()
        context['impactos_modulo_accesorio_antena'] = Impacto.objects.filter(w_fc_imp=week, tipo_impacto=MODULO_ACCESORIO_ANTENA).order_by('estacion_id').distinct('estacion').count()
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
    impactos_si = [Impacto.objects.filter(**{w_fc:week, 'impactado':SI}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    impactos_no = [Estacion.objects.filter(**{w_fc:week}).count() - Impacto.objects.filter(**{w_fc:week, 'impactado':SI}).order_by('estacion_id').distinct('estacion').count() for week in weeks if int(week) >= WEEK]
    data = {
        'labels': labels,
        'impactos_si': impactos_si,
        'impactos_no': impactos_no,
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
