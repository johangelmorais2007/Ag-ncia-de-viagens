from django.contrib import admin
from .models import Viagem, ImagemViagem

@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = ("nome_pais", "tempo", "preco", "criado_em")
    search_fields = ("nome_pais",)
    list_filter = ("tempo",)

@admin.register(ImagemViagem)
class ImagemViagemAdmin(admin.ModelAdmin):
    list_display = ("viagem",)
