from django import forms
from django.forms import ModelForm
from .models import ConsumoNokia, ConsumoClaro

class ConsumoNokiaForm(ModelForm):
    class Meta:
        model = ConsumoNokia
        fields = '__all__'

class FilterConsumoNokiaForm(ModelForm):
    class Meta:
        model = ConsumoNokia
        fields = ('parte', 'grupo_parte')

class ConsumoClaroForm(ModelForm):
    class Meta:
        model = ConsumoClaro
        fields = '__all__'

class FilterConsumoClaroForm(ModelForm):
    class Meta:
        model = ConsumoClaro
        fields = ('parte', 'grupo_parte')
