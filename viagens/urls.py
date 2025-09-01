from django.urls import path
from . import views

urlpatterns = [
    path("lista/", views.lista_viagens, name="lista_viagens"),
    path("nova/", views.criar_viagem, name="criar_viagem"),
    path("agendar/<int:viagem_id>/", views.agendar_viagem, name="agendar_viagem"),
    path("minhas/", views.minhas_viagens, name="minhas_viagens"),
]
