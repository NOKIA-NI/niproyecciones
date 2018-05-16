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
        queryset = Parte.objects.all()
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
                          (Q(impactar__icontains=q) for q in query_list))
            )
        result = queryset.count()
        context['result'] = result
        return context

class FilterParte(ListParte):

    def get_queryset(self):
        queryset = super(FilterParte, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterParte, self).get_context_data(**kwargs)
        queryset = Parte.objects.all()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        queryset = queryset.filter(**query_dict)
        result = queryset.count()
        context['query_dict'] = query_dict
        context['result'] = result
        return context

def export_parte(request):
    parte_resource = ParteResource()
    query_dict = request.GET.dict()
    queryset = Parte.objects.filter(**query_dict)
    dataset = parte_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Parte.xlsx"'
    return response
