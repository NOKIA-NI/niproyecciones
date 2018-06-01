from django.shortcuts import render
from django.views.generic import (
TemplateView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView,
FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LlegadaForm, FilterLlegadaForm
from .models import Llegada
import operator
from django.db.models import Q
from functools import reduce
from .resources import LlegadaResource
from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == settings.VIERNES or WEEKDAY == settings.SABADO or WEEKDAY == settings.DOMINGO:
    WEEK = WEEK + 1

class ListLlegada(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = Llegada
    template_name = 'llegada/list_llegada.html'
    paginate_by = 15
    form_class = FilterLlegadaForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListLlegada, self).get_context_data(**kwargs)
        weeks = list(range(14, 53))
        week = WEEK
        fields = [week for week in weeks if week >= WEEK]
        context['fields'] = fields
        context['week'] = week
        context['items'] = self.get_queryset
        context['all_items'] = str(Llegada.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailLlegada(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Llegada
    template_name = 'llegada/detail_llegada.html'

class CreateLlegada(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = LlegadaForm
    template_name = 'llegada/includes/partials/create_llegada.html'

class UpdateLlegada(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Llegada
    form_class = LlegadaForm
    template_name = 'llegada/includes/partials/update_llegada.html'

class DeleteLlegada(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Llegada
    template_name = 'llegada/includes/partials/delete_llegada.html'

class SearchLlegada(ListLlegada):

    def get_queryset(self):
        queryset = super(SearchLlegada, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(grupo_parte__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchLlegada, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterLlegada(ListLlegada):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterLlegada, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterLlegada, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_llegada(request):
    llegada_resource = LlegadaResource()
    query_dict = request.GET.dict()
    queryset = Llegada.objects.filter(**query_dict)
    dataset = llegada_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Llegada.xlsx"'
    return response
