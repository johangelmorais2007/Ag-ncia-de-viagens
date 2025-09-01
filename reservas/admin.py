from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("usuario", "viagem", "pais_custom", "criado_em")
    list_filter = ("criado_em",)
