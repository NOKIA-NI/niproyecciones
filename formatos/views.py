from django.shortcuts import render
from django.http import HttpResponse
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
from .forms import FormatoEstacionForm, FormatoParteForm, FormatoClaroForm
from .models import FormatoEstacion, FormatoParte, FormatoClaro
from proyecciones.models import Proyeccion
from estaciones.models import Estacion
from partes.models import Parte
from django.db.models import Sum, Value as V
from django.db.models.functions import Coalesce
import operator
from django.db.models import Q
from functools import reduce
from .resources import FormatoEstacionResource, FormatoParteResource, FormatoClaroResource
from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == settings.VIERNES or WEEKDAY == settings.SABADO or WEEKDAY == settings.DOMINGO:
    WEEK = WEEK + 1

PENDIENTEPEDIDO = 'Pendiente Pedido'

class ListFormatoEstacion(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = FormatoEstacion
    template_name = 'formato_estacion/list_formato_estacion.html'
    paginate_by = 15
    form_class = FormatoEstacionForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListFormatoEstacion, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(FormatoEstacion.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class SearchFormatoEstacion(ListFormatoEstacion):

    def get_queryset(self):
        queryset = super(SearchFormatoEstacion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__site_name__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchFormatoEstacion, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterFormatoEstacion(ListFormatoEstacion):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterFormatoEstacion, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterFormatoEstacion, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_formato_estacion(request):
    formato_estacion_resource = FormatoEstacionResource()
    query_dict = request.GET.dict()
    queryset = FormatoEstacion.objects.filter(**query_dict)
    dataset = formato_estacion_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="FormatoEstacion.xlsx"'
    return response

def create_formato_estacion(request):
    weeks = list(range(14, 53))

    for week in weeks:
        if week >= WEEK:
            proyecciones = Proyeccion.objects.filter(estacion__w_fc_imp=week, estacion__bolsa=PENDIENTEPEDIDO).order_by('estacion_id').distinct('estacion')
            for proyeccion in proyecciones:
                try:
                    formato_estacion = FormatoEstacion.objects.get(estacion=proyeccion.estacion)
                except FormatoEstacion.DoesNotExist:
                    formato_estacion = FormatoEstacion.objects.create(
                    estacion = proyeccion.estacion,
                    )

    return HttpResponse(status=204)

class ListFormatoParte(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = FormatoParte
    template_name = 'formato_parte/list_formato_parte.html'
    paginate_by = 15
    form_class = FormatoParteForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListFormatoParte, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(FormatoParte.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class SearchFormatoParte(ListFormatoParte):

    def get_queryset(self):
        queryset = super(SearchFormatoParte, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(formato_estacion__estacion__site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchFormatoParte, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterFormatoParte(ListFormatoParte):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterFormatoParte, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterFormatoParte, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_formato_parte(request):
    formato_parte_resource = FormatoParteResource()
    query_dict = request.GET.dict()
    queryset = FormatoParte.objects.filter(**query_dict)
    dataset = formato_parte_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="FormatoParte.xlsx"'
    return response

def create_formato_parte(request):
    formatos_estacion = FormatoEstacion.objects.all()
    partes = Parte.objects.all()

    for parte in partes:
        for formato_estacion in formatos_estacion:
            proyecciones = Proyeccion.objects.filter(estacion=formato_estacion.estacion, parte=parte)
            cantidad = proyecciones.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
            if cantidad > 0:
                try:
                    formato_parte = FormatoParte.objects.get(formato_estacion=formato_estacion, parte=parte)
                except FormatoParte.DoesNotExist:
                    formato_parte = FormatoParte.objects.create(
                        formato_estacion = formato_estacion,
                        parte = parte,
                        cantidad = cantidad,
                        )

    return HttpResponse(status=204)

class ListFormatoClaro(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = FormatoClaro
    template_name = 'formato_claro/list_formato_claro.html'
    paginate_by = 15
    form_class = FormatoClaroForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListFormatoClaro, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(FormatoClaro.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class SearchFormatoClaro(ListFormatoClaro):

    def get_queryset(self):
        queryset = super(SearchFormatoClaro, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(sitio__site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyecto__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(sap__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(descripcion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ciudad__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(regional__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(semana__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(mes__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchFormatoClaro, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterFormatoClaro(ListFormatoClaro):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterFormatoClaro, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterFormatoClaro, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_formato_claro(request):
    formato_claro_resource = FormatoClaroResource()
    query_dict = request.GET.dict()
    queryset = FormatoClaro.objects.filter(**query_dict)
    dataset = formato_claro_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="FormatoClaro.xlsx"'
    return response

def create_formato_claro(request):
    formatos_parte = FormatoParte.objects.all()

    for formato_parte in formatos_parte:
        try:
            formatos_claro = FormatoClaro.objects.get(formato_parte__id=formato_parte.id)
        except FormatoClaro.DoesNotExist:
            formato_claro = FormatoClaro.objects.create(
                formato_parte = formato_parte,
                )

    return HttpResponse(status=204)
