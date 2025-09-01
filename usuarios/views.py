from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model

def cadastro(request):
    if request.method == "GET":
        return render(request, "usuarios/cadastro.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe")
            return redirect("cadastro")   # ✅ sem namespace

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        login_django(request, user)
        return redirect("home")   # ✅ leva para a home

def login_view(request):   # ✅ renomeado pra evitar conflito
    if request.method == "GET":
        return render(request, "usuarios/login.html")
    else:
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            user = authenticate(username=user.username, password=senha)
        except User.DoesNotExist:
            user = None

        if user:
            login_django(request, user)
            return redirect("home")
        else:
            messages.error(request, "Email ou senha inválidos")
            return redirect("login")   # ✅ sem namespace

@login_required(login_url="/usuarios/login/")  # ✅ usa name da rota
def usuarios_home(request):
    return render(request, "home/home.html")
