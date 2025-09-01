from django import forms
from .models import Viagem, ImagemViagem

class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ["nome_pais", "descricao", "tempo", "preco"]

class ImagemViagemForm(forms.ModelForm):
    class Meta:
        model = ImagemViagem
        fields = ["imagem"]
