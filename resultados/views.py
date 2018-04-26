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
from .forms import ResultadoForm
from .models import Resultado
import operator
from django.db.models import Q
from functools import reduce
from .resources import ResultadoResource
from django.http import HttpResponse
from partes.models import Parte

class ListResultado(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = Resultado
    template_name = 'resultado/list_resultado.html'
    paginate_by = 100

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListResultado, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

    def get_queryset(self, **kwargs):
        queryset = super(ListResultado, self).get_queryset()
        query = self.request.GET.get('qs')
        if query:
            queryset = queryset.filter(grupo_parte=query)
        return queryset

class DetailResultado(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Resultado
    template_name = 'resultado/detail_resultado.html'

class CreateResultado(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = ResultadoForm
    template_name = 'resultado/includes/partials/create_resultado.html'

class UpdateResultado(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Resultado
    form_class = ResultadoForm
    template_name = 'resultado/includes/partials/update_resultado.html'

class DeleteResultado(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Resultado
    template_name = 'resultado/includes/partials/delete_resultado.html'

class SearchResultado(ListResultado):

    def get_queryset(self):
        queryset = super(SearchResultado, self).get_queryset()
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

def export_resultado(request):
    resultado_resource = ResultadoResource()
    queryset = Resultado.objects.all()
    query = request.GET.get('qs')
    if query:
        queryset = Resultado.objects.filter(grupo_parte=query)
    dataset = resultado_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Resultado.xlsx"'
    return response

# def calculate_resultado(request):
#     partes = Parte.objects.all()
#
#     for parte in partes:
#         resultado_w14 = (parte.existencia.w14 + parte.llegada.w14) - (parte.consumonokia.w14 + parte.consumoclaro.w14)
#         resultado_w15 = (parte.existencia.w15 + parte.llegada.w15) - (parte.consumonokia.w15 + parte.consumoclaro.w15)
#         resultado_w16 = (parte.existencia.w16 + parte.llegada.w16) - (parte.consumonokia.w16 + parte.consumoclaro.w16)
#         resultado_w17 = (parte.existencia.w17 + parte.llegada.w17) - (parte.consumonokia.w17 + parte.consumoclaro.w17)
#         resultado_w18 = (parte.existencia.w18 + parte.llegada.w18) - (parte.consumonokia.w18 + parte.consumoclaro.w18)
#         resultado_w19 = (parte.existencia.w19 + parte.llegada.w19) - (parte.consumonokia.w19 + parte.consumoclaro.w19)
#         resultado_w20 = (parte.existencia.w20 + parte.llegada.w20) - (parte.consumonokia.w20 + parte.consumoclaro.w20)
#         resultado_w21 = (parte.existencia.w21 + parte.llegada.w21) - (parte.consumonokia.w21 + parte.consumoclaro.w21)
#         resultado_w22 = (parte.existencia.w22 + parte.llegada.w22) - (parte.consumonokia.w22 + parte.consumoclaro.w22)
#         resultado_w23 = (parte.existencia.w23 + parte.llegada.w23) - (parte.consumonokia.w23 + parte.consumoclaro.w23)
#         resultado_w24 = (parte.existencia.w24 + parte.llegada.w24) - (parte.consumonokia.w24 + parte.consumoclaro.w24)
#         resultado_w25 = (parte.existencia.w25 + parte.llegada.w25) - (parte.consumonokia.w25 + parte.consumoclaro.w25)
#         resultado_w26 = (parte.existencia.w26 + parte.llegada.w26) - (parte.consumonokia.w26 + parte.consumoclaro.w26)
#         resultado_w27 = (parte.existencia.w27 + parte.llegada.w27) - (parte.consumonokia.w27 + parte.consumoclaro.w27)
#         resultado_w28 = (parte.existencia.w28 + parte.llegada.w28) - (parte.consumonokia.w28 + parte.consumoclaro.w28)
#         resultado_w29 = (parte.existencia.w29 + parte.llegada.w29) - (parte.consumonokia.w29 + parte.consumoclaro.w29)
#         resultado_w30 = (parte.existencia.w30 + parte.llegada.w30) - (parte.consumonokia.w30 + parte.consumoclaro.w30)
#         resultado_w31 = (parte.existencia.w31 + parte.llegada.w31) - (parte.consumonokia.w31 + parte.consumoclaro.w31)
#         resultado_w32 = (parte.existencia.w32 + parte.llegada.w32) - (parte.consumonokia.w32 + parte.consumoclaro.w32)
#         resultado_w33 = (parte.existencia.w33 + parte.llegada.w33) - (parte.consumonokia.w33 + parte.consumoclaro.w33)
#         resultado_w34 = (parte.existencia.w34 + parte.llegada.w34) - (parte.consumonokia.w34 + parte.consumoclaro.w34)
#         resultado_w35 = (parte.existencia.w35 + parte.llegada.w35) - (parte.consumonokia.w35 + parte.consumoclaro.w35)
#         resultado_w36 = (parte.existencia.w36 + parte.llegada.w36) - (parte.consumonokia.w36 + parte.consumoclaro.w36)
#         resultado_w37 = (parte.existencia.w37 + parte.llegada.w37) - (parte.consumonokia.w37 + parte.consumoclaro.w37)
#         resultado_w38 = (parte.existencia.w38 + parte.llegada.w38) - (parte.consumonokia.w38 + parte.consumoclaro.w38)
#         resultado_w39 = (parte.existencia.w39 + parte.llegada.w39) - (parte.consumonokia.w39 + parte.consumoclaro.w39)
#         resultado_w40 = (parte.existencia.w40 + parte.llegada.w40) - (parte.consumonokia.w40 + parte.consumoclaro.w40)
#         resultado_w41 = (parte.existencia.w41 + parte.llegada.w41) - (parte.consumonokia.w41 + parte.consumoclaro.w41)
#         resultado_w42 = (parte.existencia.w42 + parte.llegada.w42) - (parte.consumonokia.w42 + parte.consumoclaro.w42)
#         resultado_w43 = (parte.existencia.w43 + parte.llegada.w43) - (parte.consumonokia.w43 + parte.consumoclaro.w43)
#         resultado_w44 = (parte.existencia.w44 + parte.llegada.w44) - (parte.consumonokia.w44 + parte.consumoclaro.w44)
#         resultado_w45 = (parte.existencia.w45 + parte.llegada.w45) - (parte.consumonokia.w45 + parte.consumoclaro.w45)
#         resultado_w46 = (parte.existencia.w46 + parte.llegada.w46) - (parte.consumonokia.w46 + parte.consumoclaro.w46)
#         resultado_w47 = (parte.existencia.w47 + parte.llegada.w47) - (parte.consumonokia.w47 + parte.consumoclaro.w47)
#         resultado_w48 = (parte.existencia.w48 + parte.llegada.w48) - (parte.consumonokia.w48 + parte.consumoclaro.w48)
#         resultado_w49 = (parte.existencia.w49 + parte.llegada.w49) - (parte.consumonokia.w49 + parte.consumoclaro.w49)
#         resultado_w50 = (parte.existencia.w50 + parte.llegada.w50) - (parte.consumonokia.w50 + parte.consumoclaro.w50)
#         resultado_w51 = (parte.existencia.w51 + parte.llegada.w51) - (parte.consumonokia.w51 + parte.consumoclaro.w51)
#         resultado_w52 = (parte.existencia.w52 + parte.llegada.w52) - (parte.consumonokia.w52 + parte.consumoclaro.w52)
#
#         parte.resultado.w14 = resultado_w14
#         parte.resultado.w15 = resultado_w15
#         parte.resultado.w16 = resultado_w16
#         parte.resultado.w17 = resultado_w17
#         parte.resultado.w18 = resultado_w18
#         parte.resultado.w19 = resultado_w19
#         parte.resultado.w20 = resultado_w20
#         parte.resultado.w21 = resultado_w21
#         parte.resultado.w22 = resultado_w22
#         parte.resultado.w23 = resultado_w23
#         parte.resultado.w24 = resultado_w24
#         parte.resultado.w25 = resultado_w25
#         parte.resultado.w26 = resultado_w26
#         parte.resultado.w27 = resultado_w27
#         parte.resultado.w28 = resultado_w28
#         parte.resultado.w29 = resultado_w29
#         parte.resultado.w30 = resultado_w30
#         parte.resultado.w31 = resultado_w31
#         parte.resultado.w32 = resultado_w32
#         parte.resultado.w33 = resultado_w33
#         parte.resultado.w34 = resultado_w34
#         parte.resultado.w35 = resultado_w35
#         parte.resultado.w36 = resultado_w36
#         parte.resultado.w37 = resultado_w37
#         parte.resultado.w38 = resultado_w38
#         parte.resultado.w39 = resultado_w39
#         parte.resultado.w40 = resultado_w40
#         parte.resultado.w41 = resultado_w41
#         parte.resultado.w42 = resultado_w42
#         parte.resultado.w43 = resultado_w43
#         parte.resultado.w44 = resultado_w44
#         parte.resultado.w45 = resultado_w45
#         parte.resultado.w46 = resultado_w46
#         parte.resultado.w47 = resultado_w47
#         parte.resultado.w48 = resultado_w48
#         parte.resultado.w49 = resultado_w49
#         parte.resultado.w50 = resultado_w50
#         parte.resultado.w51 = resultado_w51
#         parte.resultado.w52 = resultado_w52
#
#         parte.resultado.save()
#
#     return redirect('resultados:list_resultado')
