from django import forms
from django.forms import ModelForm
from .models import Consulta
from . import choices

class ConsultaForm(ModelForm):
    # database = forms.ChoiceField(choices=choices.DATABASE_CHOICES, required=False)

    class Meta:
        model = Consulta
        fields = '__all__'

class FilterConsultaForm(ModelForm):
    nombre = forms.CharField(required=False)
    
    class Meta:
        model = Consulta
        fields = ('nombre', 'tipo_consulta')
