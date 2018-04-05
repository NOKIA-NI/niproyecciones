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
from .forms import ProyeccionForm
from .models import Proyeccion
import operator
from django.db.models import Q
from functools import reduce
from .resources import ProyeccionResource
from django.http import HttpResponse

class ListProyeccion(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = Proyeccion
    template_name = 'proyeccion/list_proyeccion.html'
    paginate_by = 15

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListProyeccion, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        return context

class DetailProyeccion(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Proyeccion
    template_name = 'proyeccion/detail_proyeccion.html'

class CreateProyeccion(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = ProyeccionForm
    template_name = 'proyeccion/includes/partials/create_proyeccion.html'

class UpdateProyeccion(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Proyeccion
    form_class = ProyeccionForm
    template_name = 'proyeccion/includes/partials/update_proyeccion.html'

class DeleteProyeccion(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Proyeccion
    template_name = 'proyeccion/includes/partials/delete_proyeccion.html'

class SearchProyeccion(ListProyeccion):

    def get_queryset(self):
        queryset = super(SearchProyeccion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyecto_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(escenario__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(banda__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(agrupadores__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estado_proyeccion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cantidad_estimada__icontains=q) for q in query_list))
            )
        return queryset

def export_proyeccion(request):
    proyeccion_resource = ProyeccionResource()
    dataset = proyeccion_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Proyeccion.xlsx"'
    return response
