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
from .forms import ConsumoNokiaForm, ConsumoClaroForm
from .models import ConsumoNokia, ConsumoClaro
import operator
from django.db.models import Q
from functools import reduce
from .resources import ConsumoNokiaResource, ConsumoClaroResource
from django.http import HttpResponse

class ListConsumoNokia(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = ConsumoNokia
    template_name = 'consumo_nokia/list_consumo_nokia.html'
    paginate_by = 15

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListConsumoNokia, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        return context

class DetailConsumoNokia(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = ConsumoNokia
    template_name = 'consumo_nokia/detail_consumo_nokia.html'

class CreateConsumoNokia(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = ConsumoNokiaForm
    template_name = 'consumo_nokia/includes/partials/create_consumo_nokia.html'

class UpdateConsumoNokia(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = ConsumoNokia
    form_class = ConsumoNokiaForm
    template_name = 'consumo_nokia/includes/partials/update_consumo_nokia.html'

class DeleteConsumoNokia(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = ConsumoNokia
    template_name = 'consumo_nokia/includes/partials/delete_consumo_nokia.html'

class SearchConsumoNokia(ListConsumoNokia):

    def get_queryset(self):
        queryset = super(SearchConsumoNokia, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list))
            )
        return queryset

def export_consumo_nokia(request):
    consumo_nokia_resource = ConsumoNokiaResource()
    dataset = consumo_nokia_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ConsumoNokia.xlsx"'
    return response

class ListConsumoClaro(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = ConsumoClaro
    template_name = 'consumo_claro/list_consumo_claro.html'
    paginate_by = 15

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListConsumoClaro, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        return context

class DetailConsumoClaro(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = ConsumoClaro
    template_name = 'consumo_claro/detail_consumo_claro.html'

class CreateConsumoClaro(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = ConsumoClaroForm
    template_name = 'consumo_claro/includes/partials/create_consumo_claro.html'

class UpdateConsumoClaro(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = ConsumoClaro
    form_class = ConsumoClaroForm
    template_name = 'consumo_claro/includes/partials/update_consumo_claro.html'

class DeleteConsumoClaro(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = ConsumoClaro
    template_name = 'consumo_claro/includes/partials/delete_consumo_claro.html'

class SearchConsumoClaro(ListConsumoClaro):

    def get_queryset(self):
        queryset = super(SearchConsumoClaro, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list))
            )
        return queryset

def export_consumo_claro(request):
    consumo_claro_resource = ConsumoClaroResource()
    dataset = consumo_claro_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ConsumoClaro.xlsx"'
    return response
