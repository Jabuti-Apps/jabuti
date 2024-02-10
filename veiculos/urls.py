from django.urls import path
from . import views

urlpatterns = [

    path('', views.veiculos),
    path("<int:veiculo_id>/", views.detalhe_veiculo, name="detalhe_veiculo"),
    path('disponiveis/', views.disponiveis, name='disponiveis'),
    path('solicitar-manutencao/<int:veiculo_id>/', views.solicitar_manutencao, name='solicitar_manutencao'),
    path('criar-manutencao/<int:veiculo_id>/', views.criar_manutencao_veiculo, name='criar_manutencao_veiculo'),
]