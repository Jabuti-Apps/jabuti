from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('', include('autorizacao.urls')),

    path('admin/', admin.site.urls),

    path("veiculos/", include("veiculos.urls")),

    path("manutencao/", include("manutencao.urls")),

    path("autorizacao/", include("autorizacao.urls")),

    path("abastecimento/", include("abastecimento.urls")),

    path("agendamento/", include("agendamento.urls")),
]
