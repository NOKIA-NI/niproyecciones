from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
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
from django.contrib.messages.views import SuccessMessageMixin
from .models import Adicional
from .forms import (
    AdicionalForm,
    FilterAdicionalForm,
)
from .resources import AdicionalResource
import operator
from django.db.models import Q
from functools import reduce

class ListAdicional(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = Adicional
    template_name = 'adicional/list_adicional.html'
    paginate_by = 15
    form_class = FilterAdicionalForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListAdicional, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Adicional.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailAdicional(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Adicional
    template_name = 'adicional/detail_adicional.html'

class CreateAdicional(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    login_url = 'users:home'
    success_message = "%(adicional)s fue creada exitosamente"
    form_class = AdicionalForm
    template_name = 'adicional/includes/partials/create_adicional.html'

class UpdateAdicional(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "%(adicional)s fue actualizada exitosamente"
    model = Adicional
    form_class = AdicionalForm
    template_name = 'adicional/includes/partials/update_adicional.html'

class DeleteAdicional(LoginRequiredMixin,
                            DeleteView):
    login_url = 'users:home'
    model = Adicional
    template_name = 'adicional/includes/partials/delete_adicional.html'
    success_url = reverse_lazy('adicionales:list_adicional')

class SearchAdicional(ListAdicional):

    def get_queryset(self):
        queryset = super(SearchAdicional, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(idadicionales_hw_sv__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(siteName__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyecto__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(banda__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(escenario__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(tipo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(seccion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cantidad__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proceso__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(usuario__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchAdicional, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterAdicional(ListAdicional):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterAdicional, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterAdicional, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_adicional(request):
    adicional_resource = AdicionalResource()
    query_dict = request.GET.dict()
    queryset = Adicional.objects.filter(**query_dict)
    dataset = adicional_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Adicional.xlsx"'
    return response