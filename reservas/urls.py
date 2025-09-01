from django.urls import path
from . import views

app_name = "reservas"

urlpatterns = [
    path("list/", views.ReservaListView.as_view(), name="list"),
    path("nova/", views.ReservaCreateView.as_view(), name="create"),
]
