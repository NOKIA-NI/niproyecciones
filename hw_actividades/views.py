from django.shortcuts import render
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
from .forms import HwActividadForm, FilterHwActividadForm
from .models import HwActividad
import operator
from django.db.models import Q
from functools import reduce
from .resources import HwActividadResource
from django.http import HttpResponse
from estaciones.models import Estacion
from partes.models import Parte
# from django.http import JsonResponse
# from django.core import serializers


class ListHwActividad(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = HwActividad
    template_name = 'hw_actividad/list_hw_actividad.html'
    paginate_by = 15
    form_class = FilterHwActividadForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListHwActividad, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(HwActividad.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
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
                          (Q(lsm__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(calculo_hw__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(impactar__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cambiar_impactar__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchHwActividad, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterHwActividad(ListHwActividad):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterHwActividad, self).get_queryset()
        request_dict = self.request.GET.dict()
        hw_actividad_fileds = [field.name for field in HwActividad._meta.fields]
        estacion_fileds = [field.name for field in Estacion._meta.fields]
        parte_fileds = [field.name for field in Parte._meta.fields]
        estacion_dict = { 'estacion__'+k: v for k, v in request_dict.items() if v if k != 'impactar' if k in estacion_fileds }
        parte_dict = { 'parte__'+k: v for k, v in request_dict.items() if v if k != 'impactar' if k in parte_fileds }
        # region_dict = { 'estacion__'+k: v for k, v in request_dict.items() if v if k == 'region' }
        # bolsa_dict = { 'estacion__'+k: v for  k, v  in request_dict.items() if v if k == 'bolsa' }
        # comunidades_dict = { 'estacion__'+k: v for  k, v  in request_dict.items() if v if k == 'comunidades' }
        # satelital_dict = { 'estacion__'+k: v for  k, v  in request_dict.items() if v if k == 'satelital' }
        # w_fc_imp_dict = { 'estacion__'+k: v for  k, v  in request_dict.items() if v if k == 'w_fc_imp' }
        # w_fc_sal_dict = { 'estacion__'+k: v for  k, v  in request_dict.items() if v if k == 'w_fc_sal' }
        # grupo_parte_dict = { 'parte__'+k: v for  k, v  in request_dict.items() if v if k == 'grupo_parte' }
        query_dict = { k: v for k, v in request_dict.items() if v if k in hw_actividad_fileds }
        # query_dict = { k: v for k, v in request_dict.items()
                    #  if v
                    #  if k in hw_actividad_fileds
                    #  if k != 'page'
                    #  if k != 'paginate_by'
                    #  if k != 'region'
                    #  if k != 'bolsa'
                    #  if k != 'comunidades'
                    #  if k != 'satelital'
                    #  if k != 'w_fc_imp'
                    #  if k != 'w_fc_sal'
                    #  if k != 'grupo_parte'
                    #  }
        query_dict = dict(query_dict, **estacion_dict, **parte_dict)
        # query_dict = dict(
        #                 query_dict,
        #                 **estacion_dict,
        #                 **parte_dict,
        #                 **region_dict,
        #                 **bolsa_dict,
        #                 **comunidades_dict,
        #                 **satelital_dict,
        #                 **w_fc_imp_dict,
        #                 **w_fc_sal_dict,
        #                 **grupo_parte_dict,
        #                 )
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterHwActividad, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_hw_actividad(request):
    hw_actividad_resource = HwActividadResource()
    query_dict = request.GET.dict()
    queryset = HwActividad.objects.filter(**query_dict)
    dataset = hw_actividad_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="HwActividad.xlsx"'
    return response

# def data_hw_actividad(request):
#     raw = ''
#     queryset = HwActividad.objects.raw('SELECT * FROM hw_actividades_hwactividad')
#     return JsonResponse(serializers.serialize('json', queryset), safe=False)
