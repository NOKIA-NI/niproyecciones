from django import forms
from django.forms import ModelForm
from .models import Parte

class ParteForm(ModelForm):
    class Meta:
        model = Parte
        fields = '__all__'

class FilterParteForm(ModelForm):
    class Meta:
        model = Parte
        fields = '__all__'
