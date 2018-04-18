from django import forms
from django.forms import ModelForm
from .models import Existencia

class ExistenciaForm(ModelForm):
    class Meta:
        model = Existencia
        fields = '__all__'
