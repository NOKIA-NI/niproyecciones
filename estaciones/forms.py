from django import forms
from django.forms import ModelForm
from .models import Estacion
from . import choices

# REGION_CHOICES_EMPTY = (('', '---------'),) + choices.REGION_CHOICES

class EstacionForm(ModelForm):
    class Meta:
        model = Estacion
        fields = '__all__'

class FilterEstacionForm(ModelForm):
    # site_name = forms.CharField(required=False)
    # region = forms.ChoiceField(choices=REGION_CHOICES_EMPTY, required=False)

    class Meta:
        model = Estacion
        fields = '__all__'
