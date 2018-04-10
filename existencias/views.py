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
from .forms import ExistenciaForm
from .models import Existencia
import operator
from django.db.models import Q
from functools import reduce
from .resources import ExistenciaResource
from django.http import HttpResponse

class ListExistencia(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = Existencia
    template_name = 'existencia/list_existencia.html'
    paginate_by = 15

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListExistencia, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        return context

class DetailExistencia(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Existencia
    template_name = 'existencia/detail_existencia.html'

class CreateExistencia(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = ExistenciaForm
    template_name = 'existencia/includes/partials/create_existencia.html'

class UpdateExistencia(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Existencia
    form_class = ExistenciaForm
    template_name = 'existencia/includes/partials/update_existencia.html'

class DeleteExistencia(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Existencia
    template_name = 'existencia/includes/partials/delete_existencia.html'

class SearchExistencia(ListExistencia):

    def get_queryset(self):
        queryset = super(SearchExistencia, self).get_queryset()
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

def export_existencia(request):
    existencia_resource = ExistenciaResource()
    dataset = existencia_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Existencia.xlsx"'
    return response
