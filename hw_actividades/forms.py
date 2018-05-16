from django import forms
from django.forms import ModelForm
from .models import HwActividad
from estaciones import choices as estaciones_choices
from partes import choices as partes_choices

class HwActividadForm(ModelForm):
    
    class Meta:
        model = HwActividad
        fields = '__all__'

class FilterHwActividadForm(ModelForm):
    region = forms.ChoiceField(choices=estaciones_choices.REGION_CHOICES, required=False)
    bolsa = forms.ChoiceField(choices=estaciones_choices.BOLSA_CHOICES, required=False)
    comunidades = forms.ChoiceField(choices=estaciones_choices.COMUNIDADES_CHOICES, required=False)
    satelital = forms.ChoiceField(choices=estaciones_choices.SATELITAL_CHOICES, required=False)
    w_fc_imp = forms.IntegerField(required=False)
    w_fc_sal = forms.IntegerField(required=False)
    grupo_parte = forms.ChoiceField(choices=partes_choices.GRUPO_PARTE_CHOICES, required=False)

    class Meta:
        model = HwActividad
        fields = '__all__'
        exclude = ('proyeccion', 'proyeccion_extra',)
