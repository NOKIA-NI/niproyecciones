from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
from .forms import ProyeccionForm, FilterProyeccionForm
from .models import Proyeccion
import operator
from django.db.models import Q
from functools import reduce
from .resources import ProyeccionResource
from .tasks import send_mail_proyeccion

class ListProyeccion(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = Proyeccion
    template_name = 'proyeccion/list_proyeccion.html'
    paginate_by = 15
    form_class = FilterProyeccionForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListProyeccion, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Proyeccion.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
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
                          (Q(proyecto__icontains=q) for q in query_list)) |
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

    def get_context_data(self, **kwargs):
        context = super(SearchProyeccion, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterProyeccion(ListProyeccion):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterProyeccion, self).get_queryset()
        dict = self.request.GET.dict()
        query_dict = { k: v for k, v in dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterProyeccion, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_proyeccion(request):
    proyeccion_resource = ProyeccionResource()
    query_dict = request.GET.dict()
    queryset = Proyeccion.objects.filter(**query_dict)
    dataset = proyeccion_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Proyeccion.xlsx"'
    return response

def send_proyeccion(request):
    task = send_mail_proyeccion.delay()
    data = { 'task_id': task.id }
    return JsonResponse(data, safe=False)
