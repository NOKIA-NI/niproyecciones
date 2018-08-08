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
from .forms import ParteForm, FilterParteForm
from .models import Parte
import operator
from django.db.models import Q
from functools import reduce
from .resources import ParteResource
from django.http import HttpResponse
from hw_proyecciones.models import HwParte

class ListParte(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = Parte
    template_name = 'parte/list_parte.html'
    paginate_by = 15
    form_class = FilterParteForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListParte, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Parte.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailParte(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Parte
    template_name = 'parte/detail_parte.html'

class CreateParte(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = ParteForm
    template_name = 'parte/includes/partials/create_parte.html'

class UpdateParte(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Parte
    form_class = ParteForm
    template_name = 'parte/includes/partials/update_parte.html'

class DeleteParte(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Parte
    template_name = 'parte/includes/partials/delete_parte.html'

class SearchParte(ListParte):

    def get_queryset(self):
        queryset = super(SearchParte, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cod_sap__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(capex__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(grupo_parte__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(grupo_familia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(grupo_numero__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchParte, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterParte(ListParte):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterParte, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterParte, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_parte(request):
    parte_resource = ParteResource()
    query_dict = request.GET.dict()
    queryset = Parte.objects.filter(**query_dict)
    dataset = parte_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Parte.xlsx"'
    return response

def create_hw_parte(request):
    hw_partes = HwParte.objects.all()
    partes = Parte.objects.all()
    for hw_parte in hw_partes:
        try:
            parte = partes.get(parte_nokia__iexact=hw_parte.nombre_nokia)
        except Parte.DoesNotExist:
            parte = Parte.objects.create(
                cod_sap=hw_parte.cod_capex,
                parte_nokia=hw_parte.nombre_nokia,
                capex=hw_parte.nombre_capex,
            )
    return HttpResponse(status=204)

def update_hw_parte(request):
    hw_partes = HwParte.objects.all()
    partes = Parte.objects.all()
    for hw_parte in hw_partes:
        try:
            parte = partes.get(parte_nokia__iexact=hw_parte.nombre_nokia)
            if parte.cod_sap != hw_parte.cod_capex or \
                parte.parte_nokia != hw_parte.nombre_nokia or \
                parte.capex != hw_parte.nombre_capex:

                parte.cod_sap = hw_parte.cod_capex
                parte.parte_nokia = hw_parte.nombre_nokia
                parte.capex = hw_parte.nombre_capex
                parte.save()

        except Parte.DoesNotExist:
            pass
    return HttpResponse(status=204)

def delete_hw_parte(request):
    hw_partes = HwParte.objects.all()
    partes = Parte.objects.all()
    for hw_parte in hw_partes:
        try:
            partes = partes.exclude(parte_nokia__iexact=hw_parte.nombre_nokia)
        except Estacion.DoesNotExist:
            pass
    partes.delete()
    return HttpResponse(status=204)
