from django import forms
from .models import Viagem

class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ["pais", "valor", "data_viagem", "tipo"]
