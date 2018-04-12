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
from .forms import LlegadaForm
from .models import Llegada
import operator
from django.db.models import Q
from functools import reduce
from .resources import LlegadaResource
from django.http import HttpResponse

class ListLlegada(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = Llegada
    template_name = 'llegada/list_llegada.html'
    paginate_by = 100

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListLlegada, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
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

def export_llegada(request):
    llegada_resource = LlegadaResource()
    dataset = llegada_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Llegada.xlsx"'
    return response
