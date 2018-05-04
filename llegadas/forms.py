from django import forms
from django.forms import ModelForm
from .models import Llegada

class LlegadaForm(ModelForm):
    class Meta:
        model = Llegada
        fields = '__all__'

class FilterLlegadaForm(ModelForm):
    class Meta:
        model = Llegada
        fields = ('parte', 'grupo_parte')
