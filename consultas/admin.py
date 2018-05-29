from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
   pass
