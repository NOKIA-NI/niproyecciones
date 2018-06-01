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
from .forms import DisponibleForm
from .models import Disponible
import operator
from django.db.models import Q
from functools import reduce
from .resources import DisponibleResource
from django.http import HttpResponse
from partes.models import Parte
from django.utils import timezone
from django.conf import settings

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == settings.VIERNES or WEEKDAY == settings.SABADO or WEEKDAY == settings.DOMINGO:
    WEEK = WEEK + 1

class ListDisponible(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = Disponible
    template_name = 'disponible/list_disponible.html'
    paginate_by = 15

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListDisponible, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class DetailDisponible(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Disponible
    template_name = 'disponible/detail_disponible.html'

class CreateDisponible(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = DisponibleForm
    template_name = 'disponible/includes/partials/create_disponible.html'

class UpdateDisponible(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Disponible
    form_class = DisponibleForm
    template_name = 'disponible/includes/partials/update_disponible.html'

class DeleteDisponible(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Disponible
    template_name = 'disponible/includes/partials/delete_disponible.html'

class SearchDisponible(ListDisponible):

    def get_queryset(self):
        queryset = super(SearchDisponible, self).get_queryset()
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

def export_disponible(request):
    disponible_resource = DisponibleResource()
    dataset = disponible_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Disponible.xlsx"'
    return response

def calculate_disponible(request):
    partes = Parte.objects.all()

    for parte in partes:
        disponible_w14 = (parte.resultado.w14 + parte.llegada.w14) - (parte.consumonokia.w14 + parte.consumoclaro.w14)
        disponible_w15 = (parte.resultado.w14 + parte.llegada.w15) - (parte.consumonokia.w15 + parte.consumoclaro.w15)
        disponible_w16 = (parte.resultado.w15 + parte.llegada.w16) - (parte.consumonokia.w16 + parte.consumoclaro.w16)
        disponible_w17 = (parte.resultado.w16 + parte.llegada.w17) - (parte.consumonokia.w17 + parte.consumoclaro.w17)
        disponible_w18 = (parte.resultado.w17 + parte.llegada.w18) - (parte.consumonokia.w18 + parte.consumoclaro.w18)
        disponible_w19 = (parte.resultado.w18 + parte.llegada.w19) - (parte.consumonokia.w19 + parte.consumoclaro.w19)
        disponible_w20 = (parte.resultado.w19 + parte.llegada.w20) - (parte.consumonokia.w20 + parte.consumoclaro.w20)
        disponible_w21 = (parte.resultado.w20 + parte.llegada.w21) - (parte.consumonokia.w21 + parte.consumoclaro.w21)
        disponible_w22 = (parte.resultado.w21 + parte.llegada.w22) - (parte.consumonokia.w22 + parte.consumoclaro.w22)
        disponible_w23 = (parte.resultado.w22 + parte.llegada.w23) - (parte.consumonokia.w23 + parte.consumoclaro.w23)
        disponible_w24 = (parte.resultado.w23 + parte.llegada.w24) - (parte.consumonokia.w24 + parte.consumoclaro.w24)
        disponible_w25 = (parte.resultado.w24 + parte.llegada.w25) - (parte.consumonokia.w25 + parte.consumoclaro.w25)
        disponible_w26 = (parte.resultado.w25 + parte.llegada.w26) - (parte.consumonokia.w26 + parte.consumoclaro.w26)
        disponible_w27 = (parte.resultado.w26 + parte.llegada.w27) - (parte.consumonokia.w27 + parte.consumoclaro.w27)
        disponible_w28 = (parte.resultado.w27 + parte.llegada.w28) - (parte.consumonokia.w28 + parte.consumoclaro.w28)
        disponible_w29 = (parte.resultado.w28 + parte.llegada.w29) - (parte.consumonokia.w29 + parte.consumoclaro.w29)
        disponible_w30 = (parte.resultado.w29 + parte.llegada.w30) - (parte.consumonokia.w30 + parte.consumoclaro.w30)
        disponible_w31 = (parte.resultado.w30 + parte.llegada.w31) - (parte.consumonokia.w31 + parte.consumoclaro.w31)
        disponible_w32 = (parte.resultado.w31 + parte.llegada.w32) - (parte.consumonokia.w32 + parte.consumoclaro.w32)
        disponible_w33 = (parte.resultado.w32 + parte.llegada.w33) - (parte.consumonokia.w33 + parte.consumoclaro.w33)
        disponible_w34 = (parte.resultado.w33 + parte.llegada.w34) - (parte.consumonokia.w34 + parte.consumoclaro.w34)
        disponible_w35 = (parte.resultado.w34 + parte.llegada.w35) - (parte.consumonokia.w35 + parte.consumoclaro.w35)
        disponible_w36 = (parte.resultado.w35 + parte.llegada.w36) - (parte.consumonokia.w36 + parte.consumoclaro.w36)
        disponible_w37 = (parte.resultado.w36 + parte.llegada.w37) - (parte.consumonokia.w37 + parte.consumoclaro.w37)
        disponible_w38 = (parte.resultado.w37 + parte.llegada.w38) - (parte.consumonokia.w38 + parte.consumoclaro.w38)
        disponible_w39 = (parte.resultado.w38 + parte.llegada.w39) - (parte.consumonokia.w39 + parte.consumoclaro.w39)
        disponible_w40 = (parte.resultado.w39 + parte.llegada.w40) - (parte.consumonokia.w40 + parte.consumoclaro.w40)
        disponible_w41 = (parte.resultado.w40 + parte.llegada.w41) - (parte.consumonokia.w41 + parte.consumoclaro.w41)
        disponible_w42 = (parte.resultado.w41 + parte.llegada.w42) - (parte.consumonokia.w42 + parte.consumoclaro.w42)
        disponible_w43 = (parte.resultado.w42 + parte.llegada.w43) - (parte.consumonokia.w43 + parte.consumoclaro.w43)
        disponible_w44 = (parte.resultado.w43 + parte.llegada.w44) - (parte.consumonokia.w44 + parte.consumoclaro.w44)
        disponible_w45 = (parte.resultado.w44 + parte.llegada.w45) - (parte.consumonokia.w45 + parte.consumoclaro.w45)
        disponible_w46 = (parte.resultado.w45 + parte.llegada.w46) - (parte.consumonokia.w46 + parte.consumoclaro.w46)
        disponible_w47 = (parte.resultado.w46 + parte.llegada.w47) - (parte.consumonokia.w47 + parte.consumoclaro.w47)
        disponible_w48 = (parte.resultado.w47 + parte.llegada.w48) - (parte.consumonokia.w48 + parte.consumoclaro.w48)
        disponible_w49 = (parte.resultado.w48 + parte.llegada.w49) - (parte.consumonokia.w49 + parte.consumoclaro.w49)
        disponible_w50 = (parte.resultado.w49 + parte.llegada.w50) - (parte.consumonokia.w50 + parte.consumoclaro.w50)
        disponible_w51 = (parte.resultado.w50 + parte.llegada.w51) - (parte.consumonokia.w51 + parte.consumoclaro.w51)
        disponible_w52 = (parte.resultado.w51 + parte.llegada.w52) - (parte.consumonokia.w52 + parte.consumoclaro.w52)

        if disponible_w14 is not None and WEEK < 14:
            parte.disponible.w14 = disponible_w14
        if disponible_w15 is not None and WEEK < 15:
            parte.disponible.w15 = disponible_w15
        if disponible_w16 is not None and WEEK < 16:
            parte.disponible.w16 = disponible_w16
        if disponible_w17 is not None and WEEK < 17:
            parte.disponible.w17 = disponible_w17
        if disponible_w18 is not None and WEEK < 18:
            parte.disponible.w18 = disponible_w18
        if disponible_w19 is not None and WEEK < 19:
            parte.disponible.w19 = disponible_w19
        if disponible_w20 is not None and WEEK < 20:
            parte.disponible.w20 = disponible_w20
        if disponible_w21 is not None and WEEK < 21:
            parte.disponible.w21 = disponible_w21
        if disponible_w22 is not None and WEEK < 22:
            parte.disponible.w22 = disponible_w22
        if disponible_w23 is not None and WEEK < 23:
            parte.disponible.w23 = disponible_w23
        if disponible_w24 is not None and WEEK < 24:
            parte.disponible.w24 = disponible_w24
        if disponible_w25 is not None and WEEK < 25:
            parte.disponible.w25 = disponible_w25
        if disponible_w26 is not None and WEEK < 26:
            parte.disponible.w26 = disponible_w26
        if disponible_w27 is not None and WEEK < 27:
            parte.disponible.w27 = disponible_w27
        if disponible_w28 is not None and WEEK < 28:
            parte.disponible.w28 = disponible_w28
        if disponible_w29 is not None and WEEK < 29:
            parte.disponible.w29 = disponible_w29
        if disponible_w30 is not None and WEEK < 30:
            parte.disponible.w30 = disponible_w30
        if disponible_w31 is not None and WEEK < 31:
            parte.disponible.w31 = disponible_w31
        if disponible_w32 is not None and WEEK < 32:
            parte.disponible.w32 = disponible_w32
        if disponible_w33 is not None and WEEK < 33:
            parte.disponible.w33 = disponible_w33
        if disponible_w34 is not None and WEEK < 34:
            parte.disponible.w34 = disponible_w34
        if disponible_w35 is not None and WEEK < 35:
            parte.disponible.w35 = disponible_w35
        if disponible_w36 is not None and WEEK < 36:
            parte.disponible.w36 = disponible_w36
        if disponible_w37 is not None and WEEK < 37:
            parte.disponible.w37 = disponible_w37
        if disponible_w38 is not None and WEEK < 38:
            parte.disponible.w38 = disponible_w38
        if disponible_w39 is not None and WEEK < 39:
            parte.disponible.w39 = disponible_w39
        if disponible_w40 is not None and WEEK < 40:
            parte.disponible.w40 = disponible_w40
        if disponible_w41 is not None and WEEK < 41:
            parte.disponible.w41 = disponible_w41
        if disponible_w42 is not None and WEEK < 42:
            parte.disponible.w42 = disponible_w42
        if disponible_w43 is not None and WEEK < 43:
            parte.disponible.w43 = disponible_w43
        if disponible_w44 is not None and WEEK < 44:
            parte.disponible.w44 = disponible_w44
        if disponible_w45 is not None and WEEK < 45:
            parte.disponible.w45 = disponible_w45
        if disponible_w46 is not None and WEEK < 46:
            parte.disponible.w46 = disponible_w46
        if disponible_w47 is not None and WEEK < 47:
            parte.disponible.w47 = disponible_w47
        if disponible_w48 is not None and WEEK < 48:
            parte.disponible.w48 = disponible_w48
        if disponible_w49 is not None and WEEK < 49:
            parte.disponible.w49 = disponible_w49
        if disponible_w50 is not None and WEEK < 50:
            parte.disponible.w50 = disponible_w50
        if disponible_w51 is not None and WEEK < 51:
            parte.disponible.w51 = disponible_w51
        if disponible_w52 is not None and WEEK < 52:
            parte.disponible.w52 = disponible_w52

        parte.disponible.save()

    return redirect('disponibles:list_disponible')
