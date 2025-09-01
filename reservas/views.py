from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Reserva

class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = "reservas/list.html"
    login_url = "usuarios:login"

class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    fields = ["cliente", "data", "destino"]
    template_name = "reservas/nova.html"
    success_url = "/reservas/list/"
    login_url = "usuarios:login"
