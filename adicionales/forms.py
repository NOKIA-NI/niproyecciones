from django import forms
from django.forms import ModelForm
from .models import (
    Adicional,
)

class AdicionalForm(ModelForm):
    class Meta:
        model = Adicional
        fields = '__all__'

class FilterAdicionalForm(ModelForm):

    class Meta:
        model = Adicional
        fields = '__all__'