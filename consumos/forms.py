from django import forms
from django.forms import ModelForm
from .models import ConsumoNokia, ConsumoClaro

class ConsumoNokiaForm(ModelForm):
    class Meta:
        model = ConsumoNokia
        fields = '__all__'

class ConsumoClaroForm(ModelForm):
    class Meta:
        model = ConsumoClaro
        fields = '__all__'
