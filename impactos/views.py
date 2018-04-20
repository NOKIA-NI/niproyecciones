from django.shortcuts import render
from django.http import HttpResponse
from .models import Impacto
from partes.models import Parte
from estaciones.models import Estacion
from hw_actividades.models import HwActividad
from resultados.models import Resultado
from django.db.models import Sum, Value as V
from django.db.models.functions import Coalesce

SI = 'Si'
NO = 'No'

def create_impacto(request):
    partes = Parte.objects.all()
    estaciones = Estacion.objects.all()
    hw_actividades = HwActividad.objects.all()

    for parte in partes:

        hw_actividades = HwActividad.objects.filter(proyeccion__parte=parte)

        for hw_actividad in hw_actividades:
            if hw_actividad.impactar == SI:
                impacto = Impacto.objects.create(
                    estacion = hw_actividad.proyeccion.estacion,
                    w_fc_sal = hw_actividad.proyeccion.estacion.w_fc_sal,
                    parte = parte,
                    grupo_parte = parte.grupo_parte,
                    cantidad_estimada = hw_actividad.proyeccion.cantidad_estimada,
                )

    return HttpResponse(status=204)


def calcular_impacto(request):

    resultados = Resultado.objects.all()
    impactos = Impacto.objects.all()
    partes = Parte.objects.all()
    weeks = ['14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
             '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
             '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
             '50', '51', '52'
    ]
    for w in weeks:

        for parte in partes:

            impactos = impactos.filter(parte=parte, w_fc_sal=int(w)).order_by('-creado')
            total_partes = impactos.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
            total_resultado = resultados.values_list('w' + w, flat=True).get(parte=parte)
            if total_resultado < 0:
                for impacto in impactos:

                    if total_resultado < 0 and total_resultado < total_partes:
                        total_resultado = total_resultado + impacto.cantidad_estimada
                        impacto.impactado = SI
                        impacto.save()

        # impactos_14 = impactos.filter(parte=parte, w_fc_sal=14).order_by('-creado')
        # total_partes_14 = impactos_14.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_14 = resultados.get(parte=parte).w14
        #
        # for impacto in impactos_14:
        #
        #     if total_resultado_14 < 0 and total_resultado_14 < total_partes_14:
        #         total_resultado_14 = total_resultado_14 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_15 = impactos.filter(parte=parte, w_fc_sal=15).order_by('-creado')
        # total_partes_15 = impactos_15.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_15 = resultados.get(parte=parte).w15
        #
        # for impacto in impactos_15:
        #
        #     if total_resultado_15 < 0 and total_resultado_15 < total_partes_15:
        #         total_resultado_15 = total_resultado_15 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_16 = impactos.filter(parte=parte, w_fc_sal=16).order_by('-creado')
        # total_partes_16 = impactos_16.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_16 = resultados.get(parte=parte).w16
        #
        # for impacto in impactos_16:
        #
        #     if total_resultado_16 < 0 and total_resultado_16 < total_partes_16:
        #         total_resultado_16 = total_resultado_16 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_17 = impactos.filter(parte=parte, w_fc_sal=17).order_by('-creado')
        # total_partes_17 = impactos_17.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_17 = resultados.get(parte=parte).w17
        #
        # for impacto in impactos_17:
        #
        #     if total_resultado_17 < 0 and total_resultado_17 < total_partes_17:
        #         total_resultado_17 = total_resultado_17 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_18 = impactos.filter(parte=parte, w_fc_sal=18).order_by('-creado')
        # total_partes_18 = impactos_18.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_18 = resultados.get(parte=parte).w18
        #
        # for impacto in impactos_18:
        #
        #     if total_resultado_18 < 0 and total_resultado_18 < total_partes_18:
        #         total_resultado_18 = total_resultado_18 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_19 = impactos.filter(parte=parte, w_fc_sal=19).order_by('-creado')
        # total_partes_19 = impactos_19.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_19 = resultados.get(parte=parte).w19
        #
        # for impacto in impactos_19:
        #
        #     if total_resultado_19 < 0 and total_resultado_19 < total_partes_19:
        #         total_resultado_19 = total_resultado_19 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_20 = impactos.filter(parte=parte, w_fc_sal=20).order_by('-creado')
        # total_partes_20 = impactos_20.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_20 = resultados.get(parte=parte).w20
        #
        # for impacto in impactos_20:
        #
        #     if total_resultado_20 < 0 and total_resultado_20 < total_partes_20:
        #         total_resultado_20 = total_resultado_20 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_21 = impactos.filter(parte=parte, w_fc_sal=21).order_by('-creado')
        # total_partes_21 = impactos_21.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_21 = resultados.get(parte=parte).w21
        #
        # for impacto in impactos_21:
        #
        #     if total_resultado_21 < 0 and total_resultado_21 < total_partes_21:
        #         total_resultado_21 = total_resultado_21 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_22 = impactos.filter(parte=parte, w_fc_sal=22).order_by('-creado')
        # total_partes_22 = impactos_22.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_22 = resultados.get(parte=parte).w22
        #
        # for impacto in impactos_22:
        #
        #     if total_resultado_22 < 0 and total_resultado_22 < total_partes_22:
        #         total_resultado_22 = total_resultado_22 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_23 = impactos.filter(parte=parte, w_fc_sal=23).order_by('-creado')
        # total_partes_23 = impactos_23.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_23 = resultados.get(parte=parte).w23
        #
        # for impacto in impactos_23:
        #
        #     if total_resultado_23 < 0 and total_resultado_23 < total_partes_23:
        #         total_resultado_23 = total_resultado_23 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_24 = impactos.filter(parte=parte, w_fc_sal=24).order_by('-creado')
        # total_partes_24 = impactos_24.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_24 = resultados.get(parte=parte).w24
        #
        # for impacto in impactos_24:
        #
        #     if total_resultado_24 < 0 and total_resultado_24 < total_partes_24:
        #         total_resultado_24 = total_resultado_24 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()
        #
        # impactos_25 = impactos.filter(parte=parte, w_fc_sal=25).order_by('-creado')
        # total_partes_25 = impactos_25.aggregate(total=Coalesce(Sum('cantidad_estimada'), V(0))).get('total')
        # total_resultado_25 = resultados.get(parte=parte).w25
        #
        # for impacto in impactos_25:
        #
        #     if total_resultado_25 < 0 and total_resultado_25 < total_partes_25:
        #         total_resultado_25 = total_resultado_25 + impacto.cantidad_estimada
        #         impacto.impactado = SI
        #         impacto.save()
        #     else:
        #         impacto.impactado = NO
        #         impacto.save()

    return HttpResponse(status=204)
