from django.shortcuts import render
from django.views.generic import (
TemplateView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EstacionForm
from .models import Estacion
import operator
from django.db.models import Q
from functools import reduce
from .resources import EstacionResource
from django.http import HttpResponse
from django.utils import timezone

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
# if WEEKDAY == 5 or WEEKDAY == 6 or WEEKDAY == 7:
#     WEEK = WEEK + 1

CENTRO = 'Centro'
COSTA = 'Costa'
ORIENTE = 'Oriente'
NOR_ORIENTE = 'Nor Oriente'
NOR_OCCIDENTE = 'Nor Occidente'
SUR_OCCIDENTE = 'Sur Occidente'

class ListEstacion(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = Estacion
    template_name = 'estacion/list_estacion.html'
    paginate_by = 15

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListEstacion, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = Estacion.objects.all().count()
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailEstacion(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Estacion
    template_name = 'estacion/detail_estacion.html'

class CreateEstacion(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = EstacionForm
    template_name = 'estacion/includes/partials/create_estacion.html'

class UpdateEstacion(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Estacion
    form_class = EstacionForm
    template_name = 'estacion/includes/partials/update_estacion.html'

class DeleteEstacion(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Estacion
    template_name = 'estacion/includes/partials/delete_estacion.html'

class SearchEstacion(ListEstacion):

    def get_queryset(self):
        queryset = super(SearchEstacion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(region__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(scope_claro__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(w_fc_imp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(total_actividades__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estado_wr__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(bolsa__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(comunidades__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(satelital__icontains=q) for q in query_list))
            )
        return queryset

def export_estacion(request):
    estacion_resource = EstacionResource()
    dataset = estacion_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Estacion.xlsx"'
    return response

class CronogramaFcImpEstacion(LoginRequiredMixin, TemplateView):
    login_url = 'users:home'
    template_name = 'estacion/cronograma_estacion.html'

    def get_context_data(self, **kwargs):
        context = super(CronogramaFcImpEstacion, self).get_context_data(**kwargs)
        weeks = list(range(14, 53))
        fields = [week for week in weeks if week >= WEEK]
        context['fields'] = fields
        context['week'] = WEEK
        context['centro'] = [Estacion.objects.filter(region=CENTRO, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['costa'] = [Estacion.objects.filter(region=COSTA, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['oriente'] = [Estacion.objects.filter(region=ORIENTE, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['nor_oriente'] = [Estacion.objects.filter(region=NOR_ORIENTE, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['nor_occidente'] = [Estacion.objects.filter(region=NOR_OCCIDENTE, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['sur_occidente'] = [Estacion.objects.filter(region=SUR_OCCIDENTE, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['total'] = [Estacion.objects.filter(w_fc_imp=week).count() for week in weeks if week >= WEEK]
        return context

class CronogramaFcSalEstacion(LoginRequiredMixin, TemplateView):
    login_url = 'users:home'
    template_name = 'estacion/cronograma_estacion.html'

    def get_context_data(self, **kwargs):
        context = super(CronogramaFcSalEstacion, self).get_context_data(**kwargs)
        weeks = list(range(14, 53))
        fields = [week for week in weeks if week >= WEEK]
        context['fields'] = fields
        context['week'] = WEEK
        context['centro'] = [Estacion.objects.filter(region=CENTRO, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['costa'] = [Estacion.objects.filter(region=COSTA, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['oriente'] = [Estacion.objects.filter(region=ORIENTE, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['nor_oriente'] = [Estacion.objects.filter(region=NOR_ORIENTE, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['nor_occidente'] = [Estacion.objects.filter(region=NOR_OCCIDENTE, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['sur_occidente'] = [Estacion.objects.filter(region=SUR_OCCIDENTE, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['total'] = [Estacion.objects.filter(w_fc_sal=week).count() for week in weeks if week >= WEEK]
        return context
