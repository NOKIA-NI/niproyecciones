from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
from .models import (
    AsignacionBulk,
    AsignacionAntena,
    EstadoPo,
    PoZina,
)
from .forms import (
    AsignacionBulkForm,
    FilterAsignacionBulkForm,
    AsignacionAntenaForm,
    FilterAsignacionAntenaForm,
    EstadoPoForm,
    FilterEstadoPoForm,
    PoZinaForm,
    FilterPoZinaForm,
)
from .resources import (
    AsignacionBulkResource,
    AsignacionAntenaResource,
    EstadoPoResource,
)
from .tasks import (
    task_sitios_asignacion,
    task_sitios_po,
    task_asignacion_bolsa,
    task_sobrantes,
    task_asignacion_bulk,
)
from tareas.models import Tarea
from estaciones.models import Estacion
from partes.models import Parte
import operator
from django.db.models import Q
from functools import reduce

class ListAsignacionBulk(LoginRequiredMixin,
                            ListView,
                            FormView):
    login_url = 'users:home'
    model = AsignacionBulk
    template_name = 'asignacion_bulk/list_asignacion_bulk.html'
    paginate_by = 15
    form_class = FilterAsignacionBulkForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListAsignacionBulk, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(AsignacionBulk.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailAsignacionBulk(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = AsignacionBulk
    template_name = 'asignacion_bulk/detail_asignacion_bulk.html'

class CreateAsignacionBulk(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    login_url = 'users:home'
    success_message = "Asignacion Bulk fue creada exitosamente"
    form_class = AsignacionBulkForm
    template_name = 'asignacion_bulk/includes/partials/create_asignacion_bulk.html'

class UpdateAsignacionBulk(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "Asignacion Bulk fue actualizada exitosamente"
    model = AsignacionBulk
    form_class = AsignacionBulkForm
    template_name = 'asignacion_bulk/includes/partials/update_asignacion_bulk.html'

class DeleteAsignacionBulk(LoginRequiredMixin,
                            DeleteView):
    login_url = 'users:home'
    model = AsignacionBulk
    template_name = 'asignacion_bulk/includes/partials/delete_asignacion_bulk.html'
    success_url = reverse_lazy('asignacion_bulks:list_asignacion_bulk')

class SearchAsignacionBulk(ListAsignacionBulk):

    def get_queryset(self):
        queryset = super(SearchAsignacionBulk, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cod_sap__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(capex__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cantidad__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cod_bodega__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(bodega__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(comentario_bodega__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(so__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(po__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchAsignacionBulk, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterAsignacionBulk(ListAsignacionBulk):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterAsignacionBulk, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterAsignacionBulk, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_asignacion_bulk(request):
    asignacion_bulk_resource = AsignacionBulkResource()
    query_dict = request.GET.dict()
    queryset = AsignacionBulk.objects.filter(**query_dict)
    dataset = asignacion_bulk_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="AsignacionBulk.xlsx"'
    return response

class ListAsignacionAntena(LoginRequiredMixin,
                            ListView,
                            FormView):
    login_url = 'users:home'
    model = AsignacionAntena
    template_name = 'asignacion_antena/list_asignacion_antena.html'
    paginate_by = 15
    form_class = FilterAsignacionAntenaForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListAsignacionAntena, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(AsignacionAntena.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailAsignacionAntena(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = AsignacionAntena
    template_name = 'asignacion_antena/detail_asignacion_antena.html'

class CreateAsignacionAntena(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    login_url = 'users:home'
    success_message = "Asignacion Antena fue creada exitosamente"
    form_class = AsignacionAntenaForm
    template_name = 'asignacion_antena/includes/partials/create_asignacion_antena.html'

class UpdateAsignacionAntena(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "Asignacion Antena fue actualizada exitosamente"
    model = AsignacionAntena
    form_class = AsignacionAntenaForm
    template_name = 'asignacion_antena/includes/partials/update_asignacion_antena.html'

class DeleteAsignacionAntena(LoginRequiredMixin,
                            DeleteView):
    login_url = 'users:home'
    model = AsignacionAntena
    template_name = 'asignacion_antena/includes/partials/delete_asignacion_antena.html'
    success_url = reverse_lazy('asignacion_antenas:list_asignacion_antena')

class SearchAsignacionAntena(ListAsignacionAntena):

    def get_queryset(self):
        queryset = super(SearchAsignacionAntena, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte__parte_nokia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cod_sap__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(capex__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cantidad__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cod_bodega__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(bodega__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(familia__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(caracteristicas__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(puertos__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchAsignacionAntena, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterAsignacionAntena(ListAsignacionAntena):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterAsignacionAntena, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterAsignacionAntena, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_asignacion_antena(request):
    asignacion_antena_resource = AsignacionAntenaResource()
    query_dict = request.GET.dict()
    queryset = AsignacionAntena.objects.filter(**query_dict)
    dataset = asignacion_antena_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="AsignacionAntena.xlsx"'
    return response

class ListEstadoPo(LoginRequiredMixin,
                            ListView,
                            FormView):
    login_url = 'users:home'
    model = EstadoPo
    template_name = 'estado_po/list_estado_po.html'
    paginate_by = 15
    form_class = FilterEstadoPoForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListEstadoPo, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(EstadoPo.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailEstadoPo(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = EstadoPo
    template_name = 'estado_po/detail_estado_po.html'

class CreateEstadoPo(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    login_url = 'users:home'
    success_message = "Asignacion Antena fue creada exitosamente"
    form_class = EstadoPoForm
    template_name = 'estado_po/includes/partials/create_estado_po.html'

class UpdateEstadoPo(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "Asignacion Antena fue actualizada exitosamente"
    model = EstadoPo
    form_class = EstadoPoForm
    template_name = 'estado_po/includes/partials/update_estado_po.html'

class DeleteEstadoPo(LoginRequiredMixin,
                            DeleteView):
    login_url = 'users:home'
    model = EstadoPo
    template_name = 'estado_po/includes/partials/delete_estado_po.html'
    success_url = reverse_lazy('estado_pos:list_estado_po')

class SearchEstadoPo(ListEstadoPo):

    def get_queryset(self):
        queryset = super(SearchEstadoPo, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(numero_po__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(project__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(bts__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(bts_status__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(bts_arrival_week__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(jumper__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(jumper_status__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(jumper_arrival_week__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(fxcb__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(fxcb_status__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(customs_ceared__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(sr__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(awb__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(eta__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(delivery__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(pre_pgi__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(fc_impl__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(fxcb_qty__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(annotation__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(comprometido__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(share__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(w_reviewed__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(columna_924__icontains=q) for q in query_list))
            )
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchEstadoPo, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterEstadoPo(ListEstadoPo):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterEstadoPo, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterEstadoPo, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_estado_po(request):
    estado_po_resource = EstadoPoResource()
    query_dict = request.GET.dict()
    queryset = EstadoPo.objects.filter(**query_dict)
    dataset = estado_po_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="EstadoPo.xlsx"'
    return response

class ListPoZina(LoginRequiredMixin,
                            ListView,
                            FormView):
    login_url = 'users:home'
    model = PoZina
    template_name = 'po_zina/list_po_zina.html'
    paginate_by = 15
    form_class = FilterPoZinaForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListPoZina, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(PoZina.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailPoZina(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = PoZina
    template_name = 'po_zina/detail_po_zina.html'

class CreatePoZina(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    login_url = 'users:home'
    success_message = "Asignacion Antena fue creada exitosamente"
    form_class = PoZinaForm
    template_name = 'po_zina/includes/partials/create_po_zina.html'

class UpdatePoZina(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "Asignacion Antena fue actualizada exitosamente"
    model = PoZina
    form_class = PoZinaForm
    template_name = 'po_zina/includes/partials/update_po_zina.html'

class DeletePoZina(LoginRequiredMixin,
                            DeleteView):
    login_url = 'users:home'
    model = PoZina
    template_name = 'po_zina/includes/partials/delete_po_zina.html'
    success_url = reverse_lazy('asignaciones:list_po_zina')

class SearchPoZina(ListPoZina):

    def get_queryset(self):
        queryset = super(SearchPoZina, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(cpo_number__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(project__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(site_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(material_description__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(parte_capex__icontains=q) for q in query_list))
            )
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchPoZina, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterPoZina(ListPoZina):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterPoZina, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterPoZina, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

def export_po_zina(request):
    po_zina_resource = PoZinaResource()
    query_dict = request.GET.dict()
    queryset = PoZina.objects.filter(**query_dict)
    dataset = po_zina_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="PoZina.xlsx"'
    return response

def sitios_asignacion(request):
    tarea_id = request.GET.get('tarea_id', None)
    tarea = Tarea.objects.get(id=tarea_id)
    task = task_sitios_asignacion.delay()
    tarea.tarea_id = task.id
    tarea.save()
    data = { 'task_id': task.id }
    return JsonResponse(data, safe=False)

def sitios_po(request):
    tarea_id = request.GET.get('tarea_id', None)
    tarea = Tarea.objects.get(id=tarea_id)
    task = task_sitios_po.delay()
    tarea.tarea_id = task.id
    tarea.save()
    data = { 'task_id': task.id }
    return JsonResponse(data, safe=False)

def asignacion_bolsa(request):
    tarea_id = request.GET.get('tarea_id', None)
    tarea = Tarea.objects.get(id=tarea_id)
    task = task_asignacion_bolsa.delay()
    tarea.tarea_id = task.id
    tarea.save()
    data = { 'task_id': task.id }
    return JsonResponse(data, safe=False)

def sobrantes(request):
    tarea_id = request.GET.get('tarea_id', None)
    tarea = Tarea.objects.get(id=tarea_id)
    task = task_sobrantes.delay()
    tarea.tarea_id = task.id
    tarea.save()
    data = { 'task_id': task.id }
    return JsonResponse(data, safe=False)

def asignacion_bulk(request):
    tarea_id = request.GET.get('tarea_id', None)
    tarea = Tarea.objects.get(id=tarea_id)
    task = task_asignacion_bulk.delay()
    tarea.tarea_id = task.id
    tarea.save()
    data = { 'task_id': task.id }
    return JsonResponse(data, safe=False)