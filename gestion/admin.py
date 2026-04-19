from django.contrib import admin
from .models import Plaza

# Esto hace que las plazas aparezcan en el panel que me mostraste
@admin.register(Plaza)
class PlazaAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'ocupada', 'patente', 'hora_ingreso')