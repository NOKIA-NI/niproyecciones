from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import (
TemplateView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView,
FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Consulta
from .forms import ConsultaForm, FilterConsultaForm
import operator
from django.db.models import Q
from functools import reduce

class ListConsulta(LoginRequiredMixin,
                   PermissionRequiredMixin,
                   ListView,
                   FormView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    model = Consulta
    template_name = 'consulta/list_consulta.html'
    paginate_by = 15
    form_class = FilterConsultaForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListConsulta, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Consulta.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class SearchConsulta(ListConsulta):

    def get_queryset(self):
        queryset = super(SearchConsulta, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(descripcion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(tipo_consulta__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(database__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchConsulta, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterConsulta(ListConsulta):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterConsulta, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterConsulta, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

class DetailConsulta(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     DetailView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    model = Consulta
    template_name = 'consulta/detail_consulta.html'

    def get_object(self):
        obj = super().get_object()
        obj.save()
        return obj

class CreateConsulta(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    success_message = "%(nombre)s fue creada exitosamente"
    form_class = ConsultaForm
    template_name = 'consulta/includes/partials/create_consulta.html'

class UpdateConsulta(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    success_message = "%(nombre)s fue actualizada exitosamente"
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consulta/includes/partials/update_consulta.html'

class DeleteConsulta(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     DeleteView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    model = Consulta
    template_name = 'consulta/includes/partials/delete_consulta.html'
    success_url = reverse_lazy('consultas:list_consulta')