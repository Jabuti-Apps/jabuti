from django.urls import path
from . import views

urlpatterns = [

    path('', views.manutencao, name='manutencao'),
    path('criar-manutencao/', views.criar_manutencao, name='criar_manutencao'),
    path("update/<int:manutencao_id>/", views.update_manutencao, name="update_manutencao"),
    path("deletar/<int:manutencao_id>/", views.deletar_manutencao, name="deletar_manutencao"),
]