from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', include('autorizacao.urls')),

    path('admin/', admin.site.urls),

    path("veiculos/", include("veiculos.urls")),

    path("manutencao/", include("manutencao.urls")),

    path("autorizacao/", include("autorizacao.urls")),

    path("abastecimento/", include("abastecimento.urls")),

    path("agendamento/", include("agendamento.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
