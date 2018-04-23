from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from impactos.models import Impacto

SI = 'Si'
ACCESORIOS = 'Accesorios'
MODULOS = 'Modulos'
ANTENAS_Y_OTROS = 'Antenas y Otros'

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
    impactos_one = [
            Impacto.objects.filter(w_fc_sal=14, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=15, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=16, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=17, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=18, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=19, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=20, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=21, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=22, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=23, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=24, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=25, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=26, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=27, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=28, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=29, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=18, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=30, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=31, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=32, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=33, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=34, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=35, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=36, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=37, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=38, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=39, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=40, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=41, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=42, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=43, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=44, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=45, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=46, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=47, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=48, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=49, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=50, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=51, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=52, impactado=SI, grupo_parte=ACCESORIOS).order_by('estacion_id').distinct('estacion').count(),
    ]
    impactos_two = [
            Impacto.objects.filter(w_fc_sal=14, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=15, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=16, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=17, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=18, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=19, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=20, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=21, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=22, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=23, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=24, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=25, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=26, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=27, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=28, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=29, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=18, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=30, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=31, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=32, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=33, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=34, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=35, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=36, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=37, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=38, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=39, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=40, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=41, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=42, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=43, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=44, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=45, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=46, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=47, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=48, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=49, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=50, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=51, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=52, impactado=SI, grupo_parte=MODULOS).order_by('estacion_id').distinct('estacion').count(),
    ]
    impactos_three = [
            Impacto.objects.filter(w_fc_sal=14, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=15, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=16, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=17, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=18, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=19, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=20, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=21, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=22, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=23, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=24, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=25, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=26, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=27, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=28, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=29, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=18, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=30, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=31, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=32, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=33, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=34, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=35, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=36, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=37, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=38, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=39, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=40, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=41, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=42, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=43, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=44, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=45, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=46, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=47, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=48, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=49, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=50, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=51, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
            Impacto.objects.filter(w_fc_sal=52, impactado=SI, grupo_parte=ANTENAS_Y_OTROS).order_by('estacion_id').distinct('estacion').count(),
    ]
    data = {
        'labels': labels,
        'impactos_one': impactos_one,
        'impactos_two': impactos_two,
        'impactos_three': impactos_three,
    }
    return JsonResponse(data)
