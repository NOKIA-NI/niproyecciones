from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
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
from .models import Tarea
from .forms import TareaForm, FilterTareaForm
import operator
from django.db.models import Q
from functools import reduce
from celery.result import AsyncResult

class ListTarea(LoginRequiredMixin,
                            ListView,
                            FormView):
    login_url = 'users:home'
    model = Tarea
    template_name = 'tarea/list_tarea.html'
    paginate_by = 15
    form_class = FilterTareaForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(ListTarea, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Tarea.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context

class SearchTarea(ListTarea):

    def get_queryset(self):
        queryset = super(SearchTarea, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(grupo_tarea__nombre__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchTarea, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context

class FilterTarea(ListTarea):
    query_dict = {}

    def get_queryset(self):
        queryset = super(FilterTarea, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = { k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by' }
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterTarea, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context

class DetailTarea(LoginRequiredMixin, DetailView):
    login_url = 'users:home'
    model = Tarea
    template_name = 'tarea/detail_tarea.html'

def get_task_status(request):
    task_id = request.GET.get('task_id', None)
    task = AsyncResult(task_id)
    data = {
        'state': task.state,
        'result': task.result,
    }
    return JsonResponse(data, safe=False)
