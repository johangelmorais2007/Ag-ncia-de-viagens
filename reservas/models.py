from django.db import models
from django.contrib.auth.models import User
from viagens.models import Viagem

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    viagem = models.ForeignKey(Viagem, on_delete=models.SET_NULL, null=True, blank=True)

    # caso usuário crie a própria viagem
    pais_custom = models.CharField(max_length=100, blank=True, null=True)
    tempo_custom = models.CharField(max_length=10, blank=True, null=True)
    preco_custom = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.viagem:
            return f"Reserva de {self.usuario.username} para {self.viagem.nome_pais}"
        return f"Reserva personalizada de {self.usuario.username}"
