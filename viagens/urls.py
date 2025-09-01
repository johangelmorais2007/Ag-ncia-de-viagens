from django.urls import path
from . import views

app_name = "viagens"

urlpatterns = [
    path("lista/", views.ViagemListView.as_view(), name="list"),
    path("nova/", views.ViagemCreateView.as_view(), name="create"),
    path("<int:pk>/editar/", views.ViagemUpdateView.as_view(), name="update"),
    path("<int:pk>/deletar/", views.ViagemDeleteView.as_view(), name="delete"),
]
