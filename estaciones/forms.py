from django import forms
from django.forms import ModelForm
from .models import Estacion

class EstacionForm(ModelForm):
    class Meta:
        model = Estacion
        fields = '__all__'
