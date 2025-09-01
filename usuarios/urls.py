from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login_view, name="login"),   # ✅ name simples
    path("home/", views.usuarios_home, name="usuarios_home"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
]
