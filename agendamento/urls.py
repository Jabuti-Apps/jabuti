from django.urls import path
from . import views


urlpatterns = [

    path("solicitar/", views.criar_agendamento, name="agendamento"),
    path("", views.agendamentos, name="agendamentos"),
    path("deletar/<int:agendamento_id>/", views.deletar_agendamento, name="deletar_agendamento"),
    path("finalizar_agendamento/<int:agendamento_id>/", views.finalizar_agendamento, name="finalizar_agendamento"),
    path("<int:agendamento_id>/", views.detalhe_agendamento, name="detalhe_agendamento")
]