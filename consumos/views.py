from django.shortcuts import render, redirect
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
from .forms import ConsumoNokiaForm, ConsumoClaroForm, FilterConsumoNokiaForm, FilterConsumoClaroForm
from .models import ConsumoNokia, ConsumoClaro
import operator
from django.db.models import Q
from functools import reduce
from .resources import ConsumoNokiaResource, ConsumoClaroResource
from django.http import HttpResponse
from partes.models import Parte
from hw_actividades.models import HwActividad
from django.db.models import Sum
from django.utils import timezone

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == 4 or WEEKDAY == 5 or WEEKDAY == 6:
    WEEK = WEEK + 1

SI = 'Si'

class ListConsumoNokia(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = ConsumoNokia
    template_name = 'consumo_nokia/list_consumo_nokia.html'
    paginate_by = 15
    form_class = FilterConsumoNokiaForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListConsumoNokia, self).get_context_data(**kwargs)
        weeks = list(range(14, 53))
        week = WEEK
        fields = [week for week in weeks if week >= WEEK]
        context['fields'] = fields
        context['week'] = week
        context['items'] = self.get_queryset
        context['all_items'] = str(ConsumoNokia.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
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
                          (Q(parte__parte_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(grupo_parte__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchConsumoNokia, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterConsumoNokia(ListConsumoNokia):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterConsumoNokia, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterConsumoNokia, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_consumo_nokia(request):
    consumo_nokia_resource = ConsumoNokiaResource()
    query_dict = request.GET.dict()
    queryset = ConsumoNokia.objects.filter(**query_dict)
    dataset = consumo_nokia_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ConsumoNokia.xlsx"'
    return response

def calculate_consumo_nokia(request):
    partes = Parte.objects.all()

    for parte in partes:
        consumo_w14 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=14, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w15 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=15, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w16 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=16, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w17 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=17, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w18 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=18, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w19 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=19, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w20 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=20, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w21 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=21, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w22 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=22, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w23 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=23, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w24 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=24, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w25 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=25, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w26 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=26, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w27 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=27, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w28 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=28, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w29 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=29, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w30 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=30, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w31 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=31, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w32 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=32, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w33 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=33, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w34 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=34, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w35 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=35, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w36 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=36, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w37 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=37, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w38 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=38, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w39 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=39, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w40 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=40, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w41 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=41, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w42 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=42, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w43 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=43, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w44 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=44, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w45 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=45, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w46 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=46, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w47 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=47, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w48 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=48, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w49 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=49, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w50 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=50, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w51 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=51, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        consumo_w52 = HwActividad.objects.filter(impactar=SI, estacion__w_fc_sal=52, parte=parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')

        if consumo_w14 is not None:
            parte.consumonokia.w14 = consumo_w14
        else:
            parte.consumonokia.w14 = 0
        if consumo_w15 is not None:
            parte.consumonokia.w15 = consumo_w15
        else:
            parte.consumonokia.w15 = 0
        if consumo_w16 is not None:
            parte.consumonokia.w16 = consumo_w16
        else:
            parte.consumonokia.w16 = 0
        if consumo_w17 is not None:
            parte.consumonokia.w17 = consumo_w17
        else:
            parte.consumonokia.w17 = 0
        if consumo_w18 is not None:
            parte.consumonokia.w18 = consumo_w18
        else:
            parte.consumonokia.w18 = 0
        if consumo_w19 is not None:
            parte.consumonokia.w19 = consumo_w19
        else:
            parte.consumonokia.w19 = 0
        if consumo_w20 is not None:
            parte.consumonokia.w20 = consumo_w20
        else:
            parte.consumonokia.w20 = 0
        if consumo_w21 is not None:
            parte.consumonokia.w21 = consumo_w21
        else:
            parte.consumonokia.w21 = 0
        if consumo_w22 is not None:
            parte.consumonokia.w22 = consumo_w22
        else:
            parte.consumonokia.w22 = 0
        if consumo_w23 is not None:
            parte.consumonokia.w23 = consumo_w23
        else:
            parte.consumonokia.w23 = 0
        if consumo_w24 is not None:
            parte.consumonokia.w24 = consumo_w24
        else:
            parte.consumonokia.w24 = 0
        if consumo_w25 is not None:
            parte.consumonokia.w25 = consumo_w25
        else:
            parte.consumonokia.w25 = 0
        if consumo_w26 is not None:
            parte.consumonokia.w26 = consumo_w26
        else:
            parte.consumonokia.w26 = 0
        if consumo_w27 is not None:
            parte.consumonokia.w27 = consumo_w27
        else:
            parte.consumonokia.w27 = 0
        if consumo_w28 is not None:
            parte.consumonokia.w28 = consumo_w28
        else:
            parte.consumonokia.w28 = 0
        if consumo_w29 is not None:
            parte.consumonokia.w29 = consumo_w29
        else:
            parte.consumonokia.w29 = 0
        if consumo_w30 is not None:
            parte.consumonokia.w30 = consumo_w30
        else:
            parte.consumonokia.w30 = 0
        if consumo_w31 is not None:
            parte.consumonokia.w31 = consumo_w31
        else:
            parte.consumonokia.w31 = 0
        if consumo_w32 is not None:
            parte.consumonokia.w32 = consumo_w32
        else:
            parte.consumonokia.w32 = 0
        if consumo_w33 is not None:
            parte.consumonokia.w33 = consumo_w33
        else:
            parte.consumonokia.w33 = 0
        if consumo_w34 is not None:
            parte.consumonokia.w34 = consumo_w34
        else:
            parte.consumonokia.w34 = 0
        if consumo_w35 is not None:
            parte.consumonokia.w35 = consumo_w35
        else:
            parte.consumonokia.w35 = 0
        if consumo_w36 is not None:
            parte.consumonokia.w36 = consumo_w36
        else:
            parte.consumonokia.w36 = 0
        if consumo_w37 is not None:
            parte.consumonokia.w37 = consumo_w37
        else:
            parte.consumonokia.w37 = 0
        if consumo_w38 is not None:
            parte.consumonokia.w38 = consumo_w38
        else:
            parte.consumonokia.w38 = 0
        if consumo_w39 is not None:
            parte.consumonokia.w39 = consumo_w39
        else:
            parte.consumonokia.w39 = 0
        if consumo_w40 is not None:
            parte.consumonokia.w40 = consumo_w40
        else:
            parte.consumonokia.w40 = 0
        if consumo_w41 is not None:
            parte.consumonokia.w41 = consumo_w41
        else:
            parte.consumonokia.w41 = 0
        if consumo_w42 is not None:
            parte.consumonokia.w42 = consumo_w42
        else:
            parte.consumonokia.w42 = 0
        if consumo_w43 is not None:
            parte.consumonokia.w43 = consumo_w43
        else:
            parte.consumonokia.w43 = 0
        if consumo_w44 is not None:
            parte.consumonokia.w44 = consumo_w44
        else:
            parte.consumonokia.w44 = 0
        if consumo_w45 is not None:
            parte.consumonokia.w45 = consumo_w45
        else:
            parte.consumonokia.w45 = 0
        if consumo_w46 is not None:
            parte.consumonokia.w46 = consumo_w46
        else:
            parte.consumonokia.w46 = 0
        if consumo_w47 is not None:
            parte.consumonokia.w47 = consumo_w47
        else:
            parte.consumonokia.w47 = 0
        if consumo_w48 is not None:
            parte.consumonokia.w48 = consumo_w48
        else:
            parte.consumonokia.w48 = 0
        if consumo_w49 is not None:
            parte.consumonokia.w49 = consumo_w49
        else:
            parte.consumonokia.w49 = 0
        if consumo_w50 is not None:
            parte.consumonokia.w50 = consumo_w50
        else:
            parte.consumonokia.w50 = 0
        if consumo_w51 is not None:
            parte.consumonokia.w51 = consumo_w51
        else:
            parte.consumonokia.w51 = 0
        if consumo_w52 is not None:
            parte.consumonokia.w52 = consumo_w52
        else:
            parte.consumonokia.w52 = 0

        parte.consumonokia.save()

    return redirect('consumos:list_consumo_nokia')

class ListConsumoClaro(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = ConsumoClaro
    template_name = 'consumo_claro/list_consumo_claro.html'
    paginate_by = 15
    form_class = FilterConsumoClaroForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListConsumoClaro, self).get_context_data(**kwargs)
        weeks = list(range(14, 53))
        week = WEEK
        fields = [week for week in weeks if week >= WEEK]
        context['fields'] = fields
        context['week'] = week
        context['items'] = self.get_queryset
        context['all_items'] = str(ConsumoClaro.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
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

    def get_context_data(self, **kwargs):
        context = super(SearchConsumoClaro, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterConsumoClaro(ListConsumoClaro):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterConsumoClaro, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in drequest_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterConsumoClaro, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_consumo_claro(request):
    consumo_claro_resource = ConsumoClaroResource()
    query_dict = request.GET.dict()
    queryset = ConsumoClaro.objects.filter(**query_dict)
    dataset = consumo_claro_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ConsumoClaro.xlsx"'
    return response
