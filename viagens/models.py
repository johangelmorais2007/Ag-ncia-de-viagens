from django.db import models

class Viagem(models.Model):
    TIPOS_TEMPO = [
        ('curta', 'Curta'),
        ('longa', 'Longa'),
    ]

    nome_pais = models.CharField(max_length=100)
    descricao = models.TextField()
    tempo = models.CharField(max_length=10, choices=TIPOS_TEMPO)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_pais} ({self.tempo}) - R${self.preco}"

class ImagemViagem(models.Model):
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name="imagens")
    imagem = models.ImageField(upload_to="viagens/")

    def __str__(self):
        return f"Imagem de {self.viagem.nome_pais}"
