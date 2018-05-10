from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
TemplateView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView,
FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Impacto
from .forms import FilterImpactoForm
import operator
from django.db.models import Q
from functools import reduce
from .resources import ImpactoResource
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

class ListImpacto(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = Impacto
    template_name = 'impacto/list_impacto.html'
    paginate_by = 15
    form_class = FilterImpactoForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListImpacto, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Impacto.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class SearchImpacto(ListImpacto):

    def get_queryset(self):
        queryset = super(SearchImpacto, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(w_fc_sal__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(w_fc_imp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(grupo_parte__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cantidad_estimada__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(impactado__icontains=q) for q in query_list))

            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchImpacto, self).get_context_data(**kwargs)
        queryset = Impacto.objects.all()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(w_fc_sal__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(w_fc_imp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(grupo_parte__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cantidad_estimada__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(impactado__icontains=q) for q in query_list))

            )
        result = queryset.count()
        context['result'] = result
        return context

class FilterImpacto(ListImpacto):

    def get_queryset(self):
        queryset = super(FilterImpacto, self).get_queryset()
        dict = self.request.GET.dict()
        query_dict = { k: v for k, v in dict.items() if v if k != 'page' if k != 'paginate_by' }
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterImpacto, self).get_context_data(**kwargs)
        queryset = Impacto.objects.all()
        dict = self.request.GET.dict()
        query_dict = { k: v for k, v in dict.items() if v if k != 'page' if k != 'paginate_by' }
        queryset = queryset.filter(**query_dict)
        result = queryset.count()
        context['query_dict'] = query_dict
        context['result'] = result
        return context

def export_impacto(request):
    impacto_resource = ImpactoResource()
    query_dict = request.GET.dict()
    queryset = Impacto.objects.filter(**query_dict)
    dataset = impacto_resource.export(queryset)
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
                total_resultado_anterior = Resultado.objects.values_list('w' + str(week - 1), flat=True).get(parte=parte)
                total_resultado_actual = Resultado.objects.values_list('w' + str(week), flat=True).get(parte=parte)
                if parte.grupo_familia is not None:
                    resultados = Resultado.objects.filter(parte__grupo_familia=parte.grupo_familia)
                    total_resultado_actual = resultados.aggregate(total=Coalesce(Sum('w'+str(week)), V(0))).get('total')
                if total_resultado_actual < 0:
                    total_resultado = total_resultado_actual
                    if total_resultado_anterior < 0 and total_resultado_anterior > total_resultado_actual:
                        total_resultado = total_resultado_anterior - total_resultado_actual
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
