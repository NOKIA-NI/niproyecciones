from django import forms
from django.forms import ModelForm
from .models import Resultado

class ResultadoForm(ModelForm):
    class Meta:
        model = Resultado
        fields = '__all__'
