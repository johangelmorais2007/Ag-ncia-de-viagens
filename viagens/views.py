from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Viagem
from django.urls import reverse_lazy

class ViagemListView(LoginRequiredMixin, ListView):
    model = Viagem
    template_name = "viagens/list.html"
    login_url = "usuarios:login"

class ViagemCreateView(LoginRequiredMixin, CreateView):
    model = Viagem
    fields = ["destino", "data"]
    template_name = "viagens/forms.html"
    success_url = reverse_lazy("viagens:list")
    login_url = "usuarios:login"


class ViagemDeleteView(LoginRequiredMixin, DeleteView):
    model = Viagem
    template_name = "viagens/deletar.html"
    success_url = reverse_lazy("viagens:list")
    login_url = "usuarios:login"
