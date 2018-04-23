from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from impactos.models import Impacto

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = 'users:home'
    template_name = 'dashboard/dashboard.html'

# def get_data(request):
#     impactos_14 = Impacto.objects.filter(w_fc_sal=14)
#     return JsonResponse(serializers.serialize('json', impactos_14), safe=False)

def get_data(request):
    labels = ['14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
             '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
             '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
             '50', '51', '52']
    impactos = [
            Impacto.objects.filter(w_fc_sal=14).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=15).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=15).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=16).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=17).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=18).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=19).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=20).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=21).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=22).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=23).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=24).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=25).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=26).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=27).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=28).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=29).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=18).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=30).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=31).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=32).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=33).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=34).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=35).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=36).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=37).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=38).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=39).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=40).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=41).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=42).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=43).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=44).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=45).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=46).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=47).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=48).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=49).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=50).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=51).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=52).order_by('estacion_id').distinct('estacion').count(),
    ]
    data = {
        'labels': labels,
        'impactos': impactos,
    }
    return JsonResponse(data)
