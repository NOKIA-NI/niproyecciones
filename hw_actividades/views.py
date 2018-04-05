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
from .forms import HwActividadForm
from .models import HwActividad
import operator
from django.db.models import Q
from functools import reduce
from .resources import HwActividadResource
from django.http import HttpResponse

class ListHwActividad(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = HwActividad
    template_name = 'hw_actividad/list_hw_actividad.html'
    paginate_by = 15

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListHwActividad, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        return context

class DetailHwActividad(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = HwActividad
    template_name = 'hw_actividad/detail_hw_actividad.html'

class CreateHwActividad(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = HwActividadForm
    template_name = 'hw_actividad/includes/partials/create_hw_actividad.html'

class UpdateHwActividad(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = HwActividad
    form_class = HwActividadForm
    template_name = 'hw_actividad/includes/partials/update_hw_actividad.html'

class DeleteHwActividad(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = HwActividad
    template_name = 'hw_actividad/includes/partials/delete_hw_actividad.html'

class SearchHwActividad(ListHwActividad):

    def get_queryset(self):
        queryset = super(SearchHwActividad, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyeccion__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(bolsa__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(comunidades__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(satelital__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(lsm__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(calculo_hw__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(impactar_estimada__icontains=q) for q in query_list))
            )
        return queryset

def export_hw_actividad(request):
    hw_actividad_resource = HwActividadResource()
    dataset = hw_actividad_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="HwActividad.xlsx"'
    return response
