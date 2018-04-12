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
from django.utils import timezone

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]

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
        existencia_w14 = (parte.resultado.w14 + parte.llegada.w14) - (parte.consumonokia.w14 + parte.consumoclaro.w14)
        existencia_w15 = (parte.resultado.w14 + parte.llegada.w15) - (parte.consumonokia.w15 + parte.consumoclaro.w15)
        existencia_w16 = (parte.resultado.w15 + parte.llegada.w16) - (parte.consumonokia.w16 + parte.consumoclaro.w16)
        existencia_w17 = (parte.resultado.w16 + parte.llegada.w17) - (parte.consumonokia.w17 + parte.consumoclaro.w17)
        existencia_w18 = (parte.resultado.w17 + parte.llegada.w18) - (parte.consumonokia.w18 + parte.consumoclaro.w18)
        existencia_w19 = (parte.resultado.w18 + parte.llegada.w19) - (parte.consumonokia.w19 + parte.consumoclaro.w19)
        existencia_w20 = (parte.resultado.w19 + parte.llegada.w20) - (parte.consumonokia.w20 + parte.consumoclaro.w20)
        existencia_w21 = (parte.resultado.w20 + parte.llegada.w21) - (parte.consumonokia.w21 + parte.consumoclaro.w21)
        existencia_w22 = (parte.resultado.w21 + parte.llegada.w22) - (parte.consumonokia.w22 + parte.consumoclaro.w22)
        existencia_w23 = (parte.resultado.w22 + parte.llegada.w23) - (parte.consumonokia.w23 + parte.consumoclaro.w23)
        existencia_w24 = (parte.resultado.w23 + parte.llegada.w24) - (parte.consumonokia.w24 + parte.consumoclaro.w24)
        existencia_w25 = (parte.resultado.w24 + parte.llegada.w25) - (parte.consumonokia.w25 + parte.consumoclaro.w25)
        existencia_w26 = (parte.resultado.w25 + parte.llegada.w26) - (parte.consumonokia.w26 + parte.consumoclaro.w26)
        existencia_w27 = (parte.resultado.w26 + parte.llegada.w27) - (parte.consumonokia.w27 + parte.consumoclaro.w27)
        existencia_w28 = (parte.resultado.w27 + parte.llegada.w28) - (parte.consumonokia.w28 + parte.consumoclaro.w28)
        existencia_w29 = (parte.resultado.w28 + parte.llegada.w29) - (parte.consumonokia.w29 + parte.consumoclaro.w29)
        existencia_w30 = (parte.resultado.w29 + parte.llegada.w30) - (parte.consumonokia.w30 + parte.consumoclaro.w30)
        existencia_w31 = (parte.resultado.w30 + parte.llegada.w31) - (parte.consumonokia.w31 + parte.consumoclaro.w31)
        existencia_w32 = (parte.resultado.w31 + parte.llegada.w32) - (parte.consumonokia.w32 + parte.consumoclaro.w32)
        existencia_w33 = (parte.resultado.w32 + parte.llegada.w33) - (parte.consumonokia.w33 + parte.consumoclaro.w33)
        existencia_w34 = (parte.resultado.w33 + parte.llegada.w34) - (parte.consumonokia.w34 + parte.consumoclaro.w34)
        existencia_w35 = (parte.resultado.w34 + parte.llegada.w35) - (parte.consumonokia.w35 + parte.consumoclaro.w35)
        existencia_w36 = (parte.resultado.w35 + parte.llegada.w36) - (parte.consumonokia.w36 + parte.consumoclaro.w36)
        existencia_w37 = (parte.resultado.w36 + parte.llegada.w37) - (parte.consumonokia.w37 + parte.consumoclaro.w37)
        existencia_w38 = (parte.resultado.w37 + parte.llegada.w38) - (parte.consumonokia.w38 + parte.consumoclaro.w38)
        existencia_w39 = (parte.resultado.w38 + parte.llegada.w39) - (parte.consumonokia.w39 + parte.consumoclaro.w39)
        existencia_w40 = (parte.resultado.w39 + parte.llegada.w40) - (parte.consumonokia.w40 + parte.consumoclaro.w40)
        existencia_w41 = (parte.resultado.w40 + parte.llegada.w41) - (parte.consumonokia.w41 + parte.consumoclaro.w41)
        existencia_w42 = (parte.resultado.w41 + parte.llegada.w42) - (parte.consumonokia.w42 + parte.consumoclaro.w42)
        existencia_w43 = (parte.resultado.w42 + parte.llegada.w43) - (parte.consumonokia.w43 + parte.consumoclaro.w43)
        existencia_w44 = (parte.resultado.w43 + parte.llegada.w44) - (parte.consumonokia.w44 + parte.consumoclaro.w44)
        existencia_w45 = (parte.resultado.w44 + parte.llegada.w45) - (parte.consumonokia.w45 + parte.consumoclaro.w45)
        existencia_w46 = (parte.resultado.w45 + parte.llegada.w46) - (parte.consumonokia.w46 + parte.consumoclaro.w46)
        existencia_w47 = (parte.resultado.w46 + parte.llegada.w47) - (parte.consumonokia.w47 + parte.consumoclaro.w47)
        existencia_w48 = (parte.resultado.w47 + parte.llegada.w48) - (parte.consumonokia.w48 + parte.consumoclaro.w48)
        existencia_w49 = (parte.resultado.w48 + parte.llegada.w49) - (parte.consumonokia.w49 + parte.consumoclaro.w49)
        existencia_w50 = (parte.resultado.w49 + parte.llegada.w50) - (parte.consumonokia.w50 + parte.consumoclaro.w50)
        existencia_w51 = (parte.resultado.w50 + parte.llegada.w51) - (parte.consumonokia.w51 + parte.consumoclaro.w51)
        existencia_w52 = (parte.resultado.w51 + parte.llegada.w52) - (parte.consumonokia.w52 + parte.consumoclaro.w52)

        if existencia_w14 is not None and WEEK < 14:
            parte.existencia.w14 = existencia_w14
        if existencia_w15 is not None and WEEK < 15:
            parte.existencia.w15 = existencia_w15
        if existencia_w16 is not None and WEEK < 16:
            parte.existencia.w16 = existencia_w16
        if existencia_w17 is not None and WEEK < 17:
            parte.existencia.w17 = existencia_w17
        if existencia_w18 is not None and WEEK < 18:
            parte.existencia.w18 = existencia_w18
        if existencia_w19 is not None and WEEK < 19:
            parte.existencia.w19 = existencia_w19
        if existencia_w20 is not None and WEEK < 20:
            parte.existencia.w20 = existencia_w20
        if existencia_w21 is not None and WEEK < 21:
            parte.existencia.w21 = existencia_w21
        if existencia_w22 is not None and WEEK < 22:
            parte.existencia.w22 = existencia_w22
        if existencia_w23 is not None and WEEK < 23:
            parte.existencia.w23 = existencia_w23
        if existencia_w24 is not None and WEEK < 24:
            parte.existencia.w24 = existencia_w24
        if existencia_w25 is not None and WEEK < 25:
            parte.existencia.w25 = existencia_w25
        if existencia_w26 is not None and WEEK < 26:
            parte.existencia.w26 = existencia_w26
        if existencia_w27 is not None and WEEK < 27:
            parte.existencia.w27 = existencia_w27
        if existencia_w28 is not None and WEEK < 28:
            parte.existencia.w28 = existencia_w28
        if existencia_w29 is not None and WEEK < 29:
            parte.existencia.w29 = existencia_w29
        if existencia_w30 is not None and WEEK < 30:
            parte.existencia.w30 = existencia_w30
        if existencia_w31 is not None and WEEK < 31:
            parte.existencia.w31 = existencia_w31
        if existencia_w32 is not None and WEEK < 32:
            parte.existencia.w32 = existencia_w32
        if existencia_w33 is not None and WEEK < 33:
            parte.existencia.w33 = existencia_w33
        if existencia_w34 is not None and WEEK < 34:
            parte.existencia.w34 = existencia_w34
        if existencia_w35 is not None and WEEK < 35:
            parte.existencia.w35 = existencia_w35
        if existencia_w36 is not None and WEEK < 36:
            parte.existencia.w36 = existencia_w36
        if existencia_w37 is not None and WEEK < 37:
            parte.existencia.w37 = existencia_w37
        if existencia_w38 is not None and WEEK < 38:
            parte.existencia.w38 = existencia_w38
        if existencia_w39 is not None and WEEK < 39:
            parte.existencia.w39 = existencia_w39
        if existencia_w40 is not None and WEEK < 40:
            parte.existencia.w40 = existencia_w40
        if existencia_w41 is not None and WEEK < 41:
            parte.existencia.w41 = existencia_w41
        if existencia_w42 is not None and WEEK < 42:
            parte.existencia.w42 = existencia_w42
        if existencia_w43 is not None and WEEK < 43:
            parte.existencia.w43 = existencia_w43
        if existencia_w44 is not None and WEEK < 44:
            parte.existencia.w44 = existencia_w44
        if existencia_w45 is not None and WEEK < 45:
            parte.existencia.w45 = existencia_w45
        if existencia_w46 is not None and WEEK < 46:
            parte.existencia.w46 = existencia_w46
        if existencia_w47 is not None and WEEK < 47:
            parte.existencia.w47 = existencia_w47
        if existencia_w48 is not None and WEEK < 48:
            parte.existencia.w48 = existencia_w48
        if existencia_w49 is not None and WEEK < 49:
            parte.existencia.w49 = existencia_w49
        if existencia_w50 is not None and WEEK < 50:
            parte.existencia.w50 = existencia_w50
        if existencia_w51 is not None and WEEK < 51:
            parte.existencia.w51 = existencia_w51
        if existencia_w52 is not None and WEEK < 52:
            parte.existencia.w52 = existencia_w52

        parte.existencia.save()

    return redirect('existencias:list_existencia')
