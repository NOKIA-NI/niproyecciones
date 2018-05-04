from django import forms
from django.forms import ModelForm
from .models import Impacto

class FilterImpactoForm(ModelForm):
    class Meta:
        model = Impacto
        fields = '__all__'
