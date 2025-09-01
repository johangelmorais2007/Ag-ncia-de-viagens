from django.contrib import admin
from django.urls import path, include
from home import views as home_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home_views.home, name="home"),

    # Apps
    path("viagens/", include("viagens.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("reservas/", include("reservas.urls")),
]
