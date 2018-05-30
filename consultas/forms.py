from django import forms
from django.forms import ModelForm
from .models import Consulta

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

class FilterConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ('nombre', 'tipo_consulta')