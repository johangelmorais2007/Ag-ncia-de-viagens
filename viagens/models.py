from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Viagem(models.Model):
    TIPO_CHOICES = (
        ("curta", "Curto prazo"),
        ("longa", "Longo prazo"),
    )
    pais = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)  # 👈 permitir nulo temporariamente
    data_viagem = models.DateField(default=timezone.now)
    tipo = models.CharField(max_length=50, default="turismo")


    def __str__(self):
        return f"{self.pais} ({self.tipo}) - {self.valor} R$"

class Agendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE)
    data_agendada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} agendou {self.viagem.pais}"
