from django.shortcuts import render
from django.urls import reverse_lazy
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
from django.contrib.messages.views import SuccessMessageMixin
from .models import Rastreo, Proceso
from .forms import RastreoForm, ProcesoForm, FilterRastreoForm, FilterProcesoForm, PerfilProcesoForm
import operator
from django.db.models import Q
from functools import reduce
from users.models import Perfil

class ListRastreo(LoginRequiredMixin,
                            ListView,
                            FormView):
    login_url = 'users:home'
    model = Rastreo
    template_name = 'rastreo/list_rastreo.html'
    paginate_by = 15
    form_class = FilterRastreoForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListRastreo, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Rastreo.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailRastreo(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Rastreo
    template_name = 'rastreo/detail_rastreo.html'

class CreateRastreo(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    login_url = 'users:home'
    success_message = "%(nombre)s fue creada exitosamente"
    form_class = RastreoForm
    template_name = 'rastreo/includes/partials/create_rastreo.html'

class UpdateRastreo(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "%(nombre)s fue actualizada exitosamente"
    model = Rastreo
    form_class = RastreoForm
    template_name = 'rastreo/includes/partials/update_rastreo.html'

class DeleteRastreo(LoginRequiredMixin,
                            DeleteView):
    login_url = 'users:home'
    model = Rastreo
    template_name = 'rastreo/includes/partials/delete_rastreo.html'
    success_url = reverse_lazy('rastreos:list_rastreo')

class SearchRastreo(ListRastreo):

    def get_queryset(self):
        queryset = super(SearchRastreo, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(responsable__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(nombre__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchRastreo, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterRastreo(ListRastreo):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterRastreo, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterRastreo, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

class ListPerfilRastreo(LoginRequiredMixin,
                            ListView,
                            FormView):
    login_url = 'users:home'
    model = Rastreo
    template_name = 'rastreo/list_perfil_rastreo.html'
    paginate_by = 15
    form_class = FilterRastreoForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self, **kwargs):
        queryset = super(ListPerfilRastreo, self).get_queryset()
        perfil = self.request.user.perfil
        queryset = queryset.filter(responsable=perfil)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListPerfilRastreo, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Rastreo.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailPerfilRastreo(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Rastreo
    template_name = 'rastreo/detail_perfil_rastreo.html'

class SearchPerfilRastreo(ListPerfilRastreo):

    def get_queryset(self):
        queryset = super(SearchPerfilRastreo, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(responsable__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(nombre__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchPerfilRastreo, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterPerfilRastreo(ListPerfilRastreo):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterPerfilRastreo, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterPerfilRastreo, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

class ListProceso(LoginRequiredMixin,
                            ListView,
                            FormView):
    login_url = 'users:home'
    model = Proceso
    template_name = 'proceso/list_proceso.html'
    paginate_by = 15
    form_class = FilterProcesoForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListProceso, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Proceso.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailProceso(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Proceso
    template_name = 'proceso/detail_proceso.html'

class CreateProceso(LoginRequiredMixin,
                            SuccessMessageMixin,
                            CreateView):
    login_url = 'users:home'
    success_message = "%(tipo_proceso)s fue creada exitosamente"
    form_class = ProcesoForm
    template_name = 'proceso/includes/partials/create_proceso.html'

    # def form_valid(self, form):
    #     form = ProcesoForm(self.request.POST, self.request.FILES)
    #     form.save()
    #     return super(CreateProceso, self).form_valid(form)

    # def form_valid(self, form):
    #     form.save(commit=True)
    #     return super(CreateProceso, self).form_valid(form)

class UpdateProceso(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "%(tipo_proceso)s fue actualizada exitosamente"
    model = Proceso
    form_class = ProcesoForm
    template_name = 'proceso/includes/partials/update_proceso.html'

class DeleteProceso(LoginRequiredMixin,
                            DeleteView):
    login_url = 'users:home'
    model = Proceso
    template_name = 'proceso/includes/partials/delete_proceso.html'
    success_url = reverse_lazy('rastreos:list_proceso')

class SearchProceso(ListProceso):

    def get_queryset(self):
        queryset = super(SearchProceso, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(rastreo__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(responsable__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(tipo_proceso__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estado_proceso__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchProceso, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterProceso(ListProceso):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterProceso, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(FilterProceso, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

class ListPerfilProceso(LoginRequiredMixin,
                            ListView,
                            FormView):
    login_url = 'users:home'
    model = Proceso
    template_name = 'proceso/list_perfil_proceso.html'
    paginate_by = 15
    form_class = FilterProcesoForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self, **kwargs):
        queryset = super(ListPerfilProceso, self).get_queryset()
        perfil = self.request.user.perfil
        queryset = queryset.filter(responsable=perfil)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListPerfilProceso, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Proceso.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class UpdatePerfilProceso(LoginRequiredMixin,
                            SuccessMessageMixin,
                            UpdateView):
    login_url = 'users:home'
    success_message = "El proceso fue actualizada exitosamente"
    model = Proceso
    form_class = PerfilProcesoForm
    template_name = 'proceso/includes/partials/update_perfil_proceso.html'

class SearchPerfilProceso(ListPerfilProceso):

    def get_queryset(self):
        queryset = super(SearchPerfilProceso, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(rastreo__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(responsable__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(tipo_proceso__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estado_proceso__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchPerfilProceso, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterPerfilProceso(ListPerfilProceso):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterPerfilProceso, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(FilterPerfilProceso, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context
