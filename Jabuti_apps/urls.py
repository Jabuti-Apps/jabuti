from django.contrib import admin
from django.urls import path, include



urlpatterns = [

    path('admin/', admin.site.urls),

    path("veiculos/", include("veiculos.urls")),

    path("manutencao/", include("manutencao.urls")),

]