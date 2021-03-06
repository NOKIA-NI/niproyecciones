from django.shortcuts import render
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
from .models import Estacion, BitacoraEstacion, ProyeccionEstacion
from .forms import (
    EstacionForm,
    FilterEstacionForm,
    BitacoraEstacionForm,
    FilterBitacoraEstacionForm,
    ProyeccionEstacionForm,
    FilterProyeccionEstacionForm,
)
from .resources import EstacionResource, BitacoraEstacionResource, ProyeccionEstacionResource
from hw_actividades.models import HwActividad
import operator
from django.db.models import Q
from functools import reduce
from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings
from hw_proyecciones.models import HwEstacion

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == settings.VIERNES or WEEKDAY == settings.SABADO or WEEKDAY == settings.DOMINGO:
    WEEK = WEEK + 1

CENTRO = 'Centro'
COSTA = 'Costa'
ORIENTE = 'Oriente'
NOR_ORIENTE = 'Nor Oriente'
NOR_OCCIDENTE = 'Nor Occidente'
SUR_OCCIDENTE = 'Sur Occidente'

class ListEstacion(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = Estacion
    template_name = 'estacion/list_estacion.html'
    paginate_by = 15
    form_class = FilterEstacionForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListEstacion, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Estacion.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        # context['estacion_form'] = self.estacion_form
        return context

class DetailEstacion(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Estacion
    template_name = 'estacion/detail_estacion.html'

class CreateEstacion(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = EstacionForm
    template_name = 'estacion/includes/partials/create_estacion.html'

class UpdateEstacion(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Estacion
    form_class = EstacionForm
    template_name = 'estacion/includes/partials/update_estacion.html'

class DeleteEstacion(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Estacion
    template_name = 'estacion/includes/partials/delete_estacion.html'

class SearchEstacion(ListEstacion):

    def get_queryset(self):
        queryset = super(SearchEstacion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(region__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ciudad__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(scope_claro__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(w_fc_sal__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(w_fc_imp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(w_fc_c__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(total_actividades__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estado_wr__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(bolsa__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(status_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(comunidades__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(satelital__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(impactar__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchEstacion, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterEstacion(ListEstacion):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterEstacion, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterEstacion, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_estacion(request):
    estacion_resource = EstacionResource()
    query_dict = request.GET.dict()
    queryset = Estacion.objects.filter(**query_dict)
    dataset = estacion_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Estacion.xlsx"'
    return response

class CronogramaFcImpEstacion(LoginRequiredMixin, TemplateView):
    login_url = 'users:home'
    template_name = 'estacion/cronograma_estacion.html'

    def get_context_data(self, **kwargs):
        context = super(CronogramaFcImpEstacion, self).get_context_data(**kwargs)
        weeks = list(range(14, 53))
        fields = [week for week in weeks if week >= WEEK]
        context['fields'] = fields
        context['week'] = WEEK
        context['centro_web'] = [Estacion.objects.filter(region=CENTRO, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['costa_web'] = [Estacion.objects.filter(region=COSTA, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['oriente_web'] = [Estacion.objects.filter(region=ORIENTE, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['nor_oriente_web'] = [Estacion.objects.filter(region=NOR_ORIENTE, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['nor_occidente_web'] = [Estacion.objects.filter(region=NOR_OCCIDENTE, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['sur_occidente_web'] = [Estacion.objects.filter(region=SUR_OCCIDENTE, w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['total_web'] = [Estacion.objects.filter(w_fc_imp=week).count() for week in weeks if week >= WEEK]
        context['suma_total_web'] = sum([Estacion.objects.filter(w_fc_imp=week).count() for week in weeks if week >= WEEK])

        context['centro_calculo_hw'] = [HwActividad.objects.filter(estacion__region=CENTRO, estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['costa_calculo_hw'] = [HwActividad.objects.filter(estacion__region=COSTA, estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['oriente_calculo_hw'] = [HwActividad.objects.filter(estacion__region=ORIENTE, estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['nor_oriente_calculo_hw'] = [HwActividad.objects.filter(estacion__region=NOR_ORIENTE, estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['nor_occidente_calculo_hw'] = [HwActividad.objects.filter(estacion__region=NOR_OCCIDENTE, estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['sur_occidente_calculo_hw'] = [HwActividad.objects.filter(estacion__region=SUR_OCCIDENTE, estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['total_calculo_hw'] = [HwActividad.objects.filter(estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['suma_total_calculo_hw'] = sum([HwActividad.objects.filter(estacion__w_fc_imp=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK])
        return context

def export_cronograma_estacion(request):
    estacion_resource = EstacionResource()
    # estaciones = [hw.estacion.id for hw in HwActividad.objects.filter(estacion__w_fc_imp__gte=WEEK).order_by('estacion_id').distinct('estacion')]
    # queryset = Estacion.objects.filter(pk__in=estaciones)
    queryset = Estacion.objects.filter(w_fc_imp__gte=WEEK)
    dataset = estacion_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Cronograma.xlsx"'
    return response

class CronogramaFcSalEstacion(LoginRequiredMixin, TemplateView):
    login_url = 'users:home'
    template_name = 'estacion/cronograma_estacion.html'

    def get_context_data(self, **kwargs):
        context = super(CronogramaFcSalEstacion, self).get_context_data(**kwargs)
        weeks = list(range(14, 53))
        fields = [week for week in weeks if week >= WEEK]
        context['fields'] = fields
        context['week'] = WEEK
        context['centro_web'] = [Estacion.objects.filter(region=CENTRO, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['costa_web'] = [Estacion.objects.filter(region=COSTA, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['oriente_web'] = [Estacion.objects.filter(region=ORIENTE, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['nor_oriente_web'] = [Estacion.objects.filter(region=NOR_ORIENTE, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['nor_occidente_web'] = [Estacion.objects.filter(region=NOR_OCCIDENTE, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['sur_occidente_web'] = [Estacion.objects.filter(region=SUR_OCCIDENTE, w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['total_web'] = [Estacion.objects.filter(w_fc_sal=week).count() for week in weeks if week >= WEEK]
        context['suma_total_web'] = sum([Estacion.objects.filter(w_fc_sal=week).count() for week in weeks if week >= WEEK])

        context['centro_calculo_hw'] = [HwActividad.objects.filter(estacion__region=CENTRO, estacion__w_fc_sal=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['costa_calculo_hw'] = [HwActividad.objects.filter(estacion__region=COSTA, estacion__w_fc_sal=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['oriente_calculo_hw'] = [HwActividad.objects.filter(estacion__region=ORIENTE, estacion__w_fc_sal=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['nor_oriente_calculo_hw'] = [HwActividad.objects.filter(estacion__region=NOR_ORIENTE, estacion__w_fc_sal=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['nor_occidente_calculo_hw'] = [HwActividad.objects.filter(estacion__region=NOR_OCCIDENTE, estacion__w_fc_sal=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['sur_occidente_calculo_hw'] = [HwActividad.objects.filter(estacion__region=SUR_OCCIDENTE, estacion__w_fc_sal=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['total_calculo_hw'] = [HwActividad.objects.filter(estacion__w_fc_sal=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK]
        context['suma_total_calculo_hw'] = sum([HwActividad.objects.filter(estacion__w_fc_sal=week).order_by('estacion_id').distinct('estacion').count() for week in weeks if week >= WEEK])
        return context

class ListBitacoraEstacion(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = BitacoraEstacion
    template_name = 'bitacora_estacion/list_bitacora_estacion.html'
    paginate_by = 15
    form_class = FilterBitacoraEstacionForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListBitacoraEstacion, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(BitacoraEstacion.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailBitacoraEstacion(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = BitacoraEstacion
    template_name = 'bitacora_estacion/detail_bitacora_estacion.html'

class CreateBitacoraEstacion(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    login_url = 'users:home'
    success_message = "%(estacion)s fue creada exitosamente"
    form_class = BitacoraEstacionForm
    template_name = 'bitacora_estacion/includes/partials/create_bitacora_estacion.html'

class UpdateBitacoraEstacion(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "%(estacion)s fue actualizada exitosamente"
    model = BitacoraEstacion
    form_class = BitacoraEstacionForm
    template_name = 'bitacora_estacion/includes/partials/update_bitacora_estacion.html'

class DeleteBitacoraEstacion(LoginRequiredMixin,
                            DeleteView):
    login_url = 'users:home'
    model = BitacoraEstacion
    template_name = 'bitacora_estacion/includes/partials/delete_bitacora_estacion.html'
    success_url = reverse_lazy('estaciones:list_bitacora_estacion')

class SearchBitacoraEstacion(ListBitacoraEstacion):

    def get_queryset(self):
        queryset = super(SearchBitacoraEstacion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(observaciones__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchBitacoraEstacion, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterBitacoraEstacion(ListBitacoraEstacion):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterBitacoraEstacion, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterBitacoraEstacion, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_bitacora_estacion(request):
    bitacora_estacion_resource = BitacoraEstacionResource()
    query_dict = request.GET.dict()
    queryset = BitacoraEstacion.objects.filter(**query_dict)
    dataset = bitacora_estacion_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="BitacoraEstacion.xlsx"'
    return response

class ListProyeccionEstacion(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = ProyeccionEstacion
    template_name = 'proyeccion_estacion/list_proyeccion_estacion.html'
    paginate_by = 15
    form_class = FilterProyeccionEstacionForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListProyeccionEstacion, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(ProyeccionEstacion.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailProyeccionEstacion(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = ProyeccionEstacion
    template_name = 'proyeccion_estacion/detail_proyeccion_estacion.html'

class CreateProyeccionEstacion(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    login_url = 'users:home'
    success_message = "%(estacion)s fue creada exitosamente"
    form_class = ProyeccionEstacionForm
    template_name = 'proyeccion_estacion/includes/partials/create_proyeccion_estacion.html'

class UpdateProyeccionEstacion(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "%(estacion)s fue actualizada exitosamente"
    model = ProyeccionEstacion
    form_class = ProyeccionEstacionForm
    template_name = 'proyeccion_estacion/includes/partials/update_proyeccion_estacion.html'

class DeleteProyeccionEstacion(LoginRequiredMixin,
                            DeleteView):
    login_url = 'users:home'
    model = ProyeccionEstacion
    template_name = 'proyeccion_estacion/includes/partials/delete_proyeccion_estacion.html'
    success_url = reverse_lazy('estaciones:list_proyeccion_estacion')

class SearchProyeccionEstacion(ListProyeccionEstacion):

    def get_queryset(self):
        queryset = super(SearchProyeccionEstacion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyeccion__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchProyeccionEstacion, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterProyeccionEstacion(ListProyeccionEstacion):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterProyeccionEstacion, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterProyeccionEstacion, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_proyeccion_estacion(request):
    proyeccion_estacion_resource = ProyeccionEstacionResource()
    query_dict = request.GET.dict()
    queryset = ProyeccionEstacion.objects.filter(**query_dict)
    dataset = proyeccion_estacion_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ProyeccionEstacion.xlsx"'
    return response

def create_hw_estacion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_estaciones = HwEstacion.objects.all()
    # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
    estaciones = Estacion.objects.all()

    for hw_estacion in hw_estaciones:
        try:
            estacion = estaciones.get(site_name__iexact=hw_estacion.siteName)
        except Estacion.DoesNotExist:
            estacion = Estacion.objects.create(
                site_name=hw_estacion.siteName,
                region=hw_estacion.region,
                ciudad=hw_estacion.ciudad,
                scope_claro=hw_estacion.scope_claro,
                w_fc_imp=hw_estacion.w_fc_c,
                w_fc_c=hw_estacion.w_fc_c,
                total_actividades=hw_estacion.actividades,
                bolsa=hw_estacion.bolsa,
                status_nokia=hw_estacion.status_nokia,
            )
    return HttpResponse(status=204)

def update_hw_estacion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_estaciones = HwEstacion.objects.all()
    # hw_proyecciones = HwProyeccion.objects.filter(created__gte=TODAY, created__lt=TOMORROW)
    estaciones = Estacion.objects.all()

    for hw_estacion in hw_estaciones:
        try:
            estacion = estaciones.get(site_name__iexact=hw_estacion.siteName)
            if estacion.site_name != hw_estacion.siteName or \
                estacion.region != hw_estacion.region or \
                estacion.ciudad != hw_estacion.ciudad or \
                estacion.scope_claro != hw_estacion.scope_claro or \
                estacion.w_fc_imp != hw_estacion.w_fc_c or \
                estacion.w_fc_c != hw_estacion.w_fc_c or \
                estacion.total_actividades != hw_estacion.actividades or \
                estacion.bolsa != hw_estacion.bolsa or \
                estacion.status_nokia != hw_estacion.status_nokia:

                estacion.site_name = hw_estacion.siteName
                estacion.region = hw_estacion.region
                estacion.ciudad = hw_estacion.ciudad
                estacion.scope_claro = hw_estacion.scope_claro
                estacion.w_fc_imp = hw_estacion.w_fc_c
                estacion.w_fc_c = hw_estacion.w_fc_c
                estacion.total_actividades = hw_estacion.actividades
                estacion.bolsa = hw_estacion.bolsa
                estacion.status_nokia = hw_estacion.status_nokia
                estacion.save()
                # estacion.w_fc_imp != hw_estacion.w_proyeccion_instalacion or \
                # estacion.w_fc_imp = hw_estacion.w_proyeccion_instalacion

        except Estacion.DoesNotExist:
            pass
    return HttpResponse(status=204)

def delete_hw_estacion(request):
    # if request.headers["X-Appengine-Cron"]:
    hw_estaciones = HwEstacion.objects.all()
    estaciones = Estacion.objects.all()

    for hw_estacion in hw_estaciones:
        try:
            estaciones = estaciones.exclude(site_name__iexact=hw_estacion.siteName)
        except Estacion.DoesNotExist:
            pass
    estaciones.delete()
    return HttpResponse(status=204)
