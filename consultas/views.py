from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from estaciones.models import Estacion


class ConsultaView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    login_url = 'users:home'
    template_name = 'consulta/list_consulta.html'
    permission_required = 'is_superuser'