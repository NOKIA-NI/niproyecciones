from django.shortcuts import render, redirect
from django.views.generic import (
TemplateView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ExistenciaForm
from .models import Existencia
import operator
from django.db.models import Q
from functools import reduce
from .resources import ExistenciaResource
from django.http import HttpResponse
from partes.models import Parte

class ListExistencia(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = Existencia
    template_name = 'existencia/list_existencia.html'
    paginate_by = 15

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListExistencia, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        return context

class DetailExistencia(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Existencia
    template_name = 'existencia/detail_existencia.html'

class CreateExistencia(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = ExistenciaForm
    template_name = 'existencia/includes/partials/create_existencia.html'

class UpdateExistencia(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Existencia
    form_class = ExistenciaForm
    template_name = 'existencia/includes/partials/update_existencia.html'

class DeleteExistencia(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Existencia
    template_name = 'existencia/includes/partials/delete_existencia.html'

class SearchExistencia(ListExistencia):

    def get_queryset(self):
        queryset = super(SearchExistencia, self).get_queryset()
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

def export_existencia(request):
    existencia_resource = ExistenciaResource()
    dataset = existencia_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Existencia.xlsx"'
    return response

def calcular_existencia(request):
    partes = Parte.objects.all()

    for parte in partes:
        existencia_w14 = (parte.consumonokia.w14 + parte.consumoclaro.w14) - (parte.llegada.w14 + parte.existencia.w14)
        existencia_w15 = (parte.consumonokia.w14 + parte.consumoclaro.w14) - (parte.llegada.w14 + parte.existencia.w14)
        existencia_w16 = (parte.consumonokia.w15 + parte.consumoclaro.w15) - (parte.llegada.w15 + parte.existencia.w15)
        existencia_w17 = (parte.consumonokia.w16 + parte.consumoclaro.w16) - (parte.llegada.w16 + parte.existencia.w16)
        existencia_w18 = (parte.consumonokia.w17 + parte.consumoclaro.w17) - (parte.llegada.w17 + parte.existencia.w17)
        existencia_w19 = (parte.consumonokia.w18 + parte.consumoclaro.w18) - (parte.llegada.w18 + parte.existencia.w18)
        existencia_w20 = (parte.consumonokia.w19 + parte.consumoclaro.w19) - (parte.llegada.w19 + parte.existencia.w19)
        existencia_w21 = (parte.consumonokia.w20 + parte.consumoclaro.w20) - (parte.llegada.w20 + parte.existencia.w20)
        existencia_w22 = (parte.consumonokia.w21 + parte.consumoclaro.w21) - (parte.llegada.w21 + parte.existencia.w21)
        existencia_w23 = (parte.consumonokia.w22 + parte.consumoclaro.w22) - (parte.llegada.w22 + parte.existencia.w22)
        existencia_w24 = (parte.consumonokia.w23 + parte.consumoclaro.w23) - (parte.llegada.w23 + parte.existencia.w23)
        existencia_w25 = (parte.consumonokia.w24 + parte.consumoclaro.w24) - (parte.llegada.w24 + parte.existencia.w24)
        existencia_w26 = (parte.consumonokia.w25 + parte.consumoclaro.w25) - (parte.llegada.w25 + parte.existencia.w25)
        existencia_w27 = (parte.consumonokia.w26 + parte.consumoclaro.w26) - (parte.llegada.w26 + parte.existencia.w26)
        existencia_w28 = (parte.consumonokia.w27 + parte.consumoclaro.w27) - (parte.llegada.w27 + parte.existencia.w27)
        existencia_w29 = (parte.consumonokia.w28 + parte.consumoclaro.w28) - (parte.llegada.w28 + parte.existencia.w28)
        existencia_w30 = (parte.consumonokia.w29 + parte.consumoclaro.w29) - (parte.llegada.w29 + parte.existencia.w29)
        existencia_w31 = (parte.consumonokia.w30 + parte.consumoclaro.w30) - (parte.llegada.w30 + parte.existencia.w30)
        existencia_w32 = (parte.consumonokia.w31 + parte.consumoclaro.w31) - (parte.llegada.w31 + parte.existencia.w31)
        existencia_w33 = (parte.consumonokia.w32 + parte.consumoclaro.w32) - (parte.llegada.w32 + parte.existencia.w32)
        existencia_w34 = (parte.consumonokia.w33 + parte.consumoclaro.w33) - (parte.llegada.w33 + parte.existencia.w33)
        existencia_w35 = (parte.consumonokia.w34 + parte.consumoclaro.w34) - (parte.llegada.w34 + parte.existencia.w34)
        existencia_w36 = (parte.consumonokia.w35 + parte.consumoclaro.w35) - (parte.llegada.w35 + parte.existencia.w35)
        existencia_w37 = (parte.consumonokia.w36 + parte.consumoclaro.w36) - (parte.llegada.w36 + parte.existencia.w36)
        existencia_w38 = (parte.consumonokia.w37 + parte.consumoclaro.w37) - (parte.llegada.w37 + parte.existencia.w37)
        existencia_w39 = (parte.consumonokia.w38 + parte.consumoclaro.w38) - (parte.llegada.w38 + parte.existencia.w38)
        existencia_w40 = (parte.consumonokia.w39 + parte.consumoclaro.w39) - (parte.llegada.w39 + parte.existencia.w39)
        existencia_w41 = (parte.consumonokia.w40 + parte.consumoclaro.w40) - (parte.llegada.w40 + parte.existencia.w40)
        existencia_w42 = (parte.consumonokia.w41 + parte.consumoclaro.w41) - (parte.llegada.w41 + parte.existencia.w41)
        existencia_w43 = (parte.consumonokia.w42 + parte.consumoclaro.w42) - (parte.llegada.w42 + parte.existencia.w42)
        existencia_w44 = (parte.consumonokia.w43 + parte.consumoclaro.w43) - (parte.llegada.w43 + parte.existencia.w43)
        existencia_w45 = (parte.consumonokia.w44 + parte.consumoclaro.w44) - (parte.llegada.w44 + parte.existencia.w44)
        existencia_w46 = (parte.consumonokia.w45 + parte.consumoclaro.w45) - (parte.llegada.w45 + parte.existencia.w45)
        existencia_w47 = (parte.consumonokia.w46 + parte.consumoclaro.w46) - (parte.llegada.w46 + parte.existencia.w46)
        existencia_w48 = (parte.consumonokia.w47 + parte.consumoclaro.w47) - (parte.llegada.w47 + parte.existencia.w47)
        existencia_w49 = (parte.consumonokia.w48 + parte.consumoclaro.w48) - (parte.llegada.w48 + parte.existencia.w48)
        existencia_w50 = (parte.consumonokia.w49 + parte.consumoclaro.w49) - (parte.llegada.w49 + parte.existencia.w49)
        existencia_w51 = (parte.consumonokia.w50 + parte.consumoclaro.w50) - (parte.llegada.w50 + parte.existencia.w50)
        existencia_w52 = (parte.consumonokia.w51 + parte.consumoclaro.w51) - (parte.llegada.w51 + parte.existencia.w51)

        if existencia_w14 is not None:
            parte.existencia.w14 = existencia_w14
        if existencia_w15 is not None:
            parte.existencia.w15 = existencia_w15
        if existencia_w16 is not None:
            parte.existencia.w16 = existencia_w16
        if existencia_w17 is not None:
            parte.existencia.w17 = existencia_w17
        if existencia_w18 is not None:
            parte.existencia.w18 = existencia_w18
        if existencia_w19 is not None:
            parte.existencia.w19 = existencia_w19
        if existencia_w20 is not None:
            parte.existencia.w20 = existencia_w20
        if existencia_w21 is not None:
            parte.existencia.w21 = existencia_w21
        if existencia_w22 is not None:
            parte.existencia.w22 = existencia_w22
        if existencia_w23 is not None:
            parte.existencia.w23 = existencia_w23
        if existencia_w24 is not None:
            parte.existencia.w24 = existencia_w24
        if existencia_w25 is not None:
            parte.existencia.w25 = existencia_w25
        if existencia_w26 is not None:
            parte.existencia.w26 = existencia_w26
        if existencia_w27 is not None:
            parte.existencia.w27 = existencia_w27
        if existencia_w28 is not None:
            parte.existencia.w28 = existencia_w28
        if existencia_w29 is not None:
            parte.existencia.w29 = existencia_w29
        if existencia_w30 is not None:
            parte.existencia.w30 = existencia_w30
        if existencia_w31 is not None:
            parte.existencia.w31 = existencia_w31
        if existencia_w32 is not None:
            parte.existencia.w32 = existencia_w32
        if existencia_w33 is not None:
            parte.existencia.w33 = existencia_w33
        if existencia_w34 is not None:
            parte.existencia.w34 = existencia_w34
        if existencia_w35 is not None:
            parte.existencia.w35 = existencia_w35
        if existencia_w36 is not None:
            parte.existencia.w36 = existencia_w36
        if existencia_w37 is not None:
            parte.existencia.w37 = existencia_w37
        if existencia_w38 is not None:
            parte.existencia.w38 = existencia_w38
        if existencia_w39 is not None:
            parte.existencia.w39 = existencia_w39
        if existencia_w40 is not None:
            parte.existencia.w40 = existencia_w40
        if existencia_w41 is not None:
            parte.existencia.w41 = existencia_w41
        if existencia_w42 is not None:
            parte.existencia.w42 = existencia_w42
        if existencia_w43 is not None:
            parte.existencia.w43 = existencia_w43
        if existencia_w44 is not None:
            parte.existencia.w44 = existencia_w44
        if existencia_w45 is not None:
            parte.existencia.w45 = existencia_w45
        if existencia_w46 is not None:
            parte.existencia.w46 = existencia_w46
        if existencia_w47 is not None:
            parte.existencia.w47 = existencia_w47
        if existencia_w48 is not None:
            parte.existencia.w48 = existencia_w48
        if existencia_w49 is not None:
            parte.existencia.w49 = existencia_w49
        if existencia_w50 is not None:
            parte.existencia.w50 = existencia_w50
        if existencia_w51 is not None:
            parte.existencia.w51 = existencia_w51
        if existencia_w52 is not None:
            parte.existencia.w52 = existencia_w52

        parte.existencia.save()

    return redirect('existencias:list_existencia')
