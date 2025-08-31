
from django.contrib import admin
from django.urls import path
from home import views as inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', inicio.home, name= "home"),
]
