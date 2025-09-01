from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Viagem, Agendamento
from .forms import ViagemForm


def lista_viagens(request):
    viagens = Viagem.objects.all()
    return render(request, "viagens/lista_viagens.html", {"viagens": viagens})


def criar_viagem(request):
    if request.method == "POST":
        form = ViagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_viagens")
    else:
        form = ViagemForm()
    return render(request, "viagens/criar_viagem.html", {"form": form})

@login_required(login_url="/usuarios/login/")
def agendar_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)
    Agendamento.objects.create(usuario=request.user, viagem=viagem)
    return redirect("minhas_viagens")

@login_required(login_url="/usuarios/login/")
def minhas_viagens(request):
    agendamentos = Agendamento.objects.filter(usuario=request.user)
    return render(request, "viagens/minhas_viagens.html", {"agendamentos": agendamentos})
