from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
TemplateView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Impacto
from partes.models import Parte
from estaciones.models import Estacion
from hw_actividades.models import HwActividad
from resultados.models import Resultado
from django.db.models import Sum, Value as V
from django.db.models.functions import Coalesce
from django.utils import timezone

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]

SI = 'Si'
NO = 'No'

class ListImpacto(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = Impacto
    template_name = 'impacto/list_impacto.html'
    paginate_by = 15

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListImpacto, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

def export_impacto(request):
    impacto_resource = ImpactoResource()
    dataset = impacto_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Impacto.xlsx"'
    return response

def create_impacto(request):
    partes = Parte.objects.all()

    for parte in partes:

        hw_actividades = HwActividad.objects.filter(impactar=SI, proyeccion__parte=parte)

        for hw_actividad in hw_actividades:
            impacto = Impacto.objects.create(
                estacion = hw_actividad.proyeccion.estacion,
                w_fc_sal = hw_actividad.proyeccion.estacion.w_fc_sal,
                w_fc_imp = hw_actividad.proyeccion.estacion.w_fc_imp,
                parte = parte,
                grupo_parte = parte.grupo_parte,
                cantidad_estimada = hw_actividad.proyeccion.cantidad_estimada,
            )

    return HttpResponse(status=204)


def calculate_impacto(request):
    partes = Parte.objects.all()
    weeks = list(range(14, 53))
    for week in weeks:
        if week >= WEEK:
            for parte in partes:
                impactos = Impacto.objects.filter(parte=parte, w_fc_sal=week).order_by('-creado')
                total_partes = impactos.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
                total_resultado = Resultado.objects.values_list('w' + str(week), flat=True).get(parte=parte)
                if total_resultado < 0:
                    for impacto in impactos:
                        if total_resultado < 0 and total_resultado < total_partes:
                            total_resultado = total_resultado + impacto.cantidad_estimada
                            impacto.impactado = SI
                            impacto.save()
                        else:
                            impacto.impactado = NO
                            impacto.save()

    return HttpResponse(status=204)


def delete_impacto(request):
    Impacto.objects.all().delete()

    return HttpResponse(status=204)
