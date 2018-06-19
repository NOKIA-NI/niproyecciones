from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import (
TemplateView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView,
FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Consulta
from .forms import ConsultaForm, FilterConsultaForm

class ListConsulta(LoginRequiredMixin,
                   PermissionRequiredMixin,
                   ListView,
                   FormView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    model = Consulta
    template_name = 'consulta/list_consulta.html'
    paginate_by = 15
    form_class = FilterConsultaForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListConsulta, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Consulta.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        # context['estacion_form'] = self.estacion_form
        return context

class DetailConsulta(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     DetailView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    model = Consulta
    template_name = 'consulta/detail_consulta.html'

class CreateConsulta(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    success_message = "%(nombre)s fue creada exitosamente"
    form_class = ConsultaForm
    template_name = 'consulta/includes/partials/create_consulta.html'
    # success_url = '/detail/consulta/'

class UpdateConsulta(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    success_message = "%(nombre)s fue actualizada exitosamente"
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consulta/includes/partials/update_consulta.html'
    # success_url = '/detail/consulta/'

class DeleteConsulta(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     DeleteView):
    login_url = 'users:home'
    permission_required = 'is_superuser'
    model = Consulta
    template_name = 'consulta/includes/partials/delete_consulta.html'
    success_url = reverse_lazy('consultas:list_consulta')