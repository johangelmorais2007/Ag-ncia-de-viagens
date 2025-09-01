from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "usuarios"

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login_view, name="login"),   # 👈 essa é a rota procurada
    path("home/", views.usuarios_home, name="usuarios_home"),
    path("logout/", LogoutView.as_view(next_page="usuarios:login"), name="logout"),
]

