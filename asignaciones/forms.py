from django import forms
from django.forms import ModelForm
from .models import (
    AsignacionBulk,
    AsignacionAntena,
    EstadoPo,
    PoZina,
)

class AsignacionBulkForm(ModelForm):
    class Meta:
        model = AsignacionBulk
        fields = '__all__'

class FilterAsignacionBulkForm(ModelForm):

    class Meta:
        model = AsignacionBulk
        fields = '__all__'

class AsignacionAntenaForm(ModelForm):
    class Meta:
        model = AsignacionAntena
        fields = '__all__'

class FilterAsignacionAntenaForm(ModelForm):

    class Meta:
        model = AsignacionAntena
        fields = '__all__'

class EstadoPoForm(ModelForm):
    class Meta:
        model = EstadoPo
        fields = '__all__'

class FilterEstadoPoForm(ModelForm):

    class Meta:
        model = EstadoPo
        fields = '__all__'

class PoZinaForm(ModelForm):
    class Meta:
        model = PoZina
        fields = '__all__'

class FilterPoZinaForm(ModelForm):

    class Meta:
        model = PoZina
        fields = '__all__'