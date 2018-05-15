from django import forms
from django.forms import ModelForm
from .models import HwActividad

class HwActividadForm(ModelForm):
    
    class Meta:
        model = HwActividad
        fields = '__all__'

class FilterHwActividadForm(ModelForm):

    class Meta:
        model = HwActividad
        fields = '__all__'
        exclude = ('proyeccion', 'proyeccion_extra',)
