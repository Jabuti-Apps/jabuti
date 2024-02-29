from django.urls import path
from . import views

urlpatterns = [
    path('', views.veiculos, name='veiculos'),
    path("<int:veiculo_id>/", views.detalhe_veiculo, name="detalhe_veiculo"),
    path('cadastrar-veiculo/', views.cadastrar_veiculo, name='cadastrar_veiculo'),
    path("update/<int:veiculo_id>/", views.update_veiculo, name="update_veiculo"),
    path("deletar/<int:veiculo_id>/", views.deletar_veiculo, name="deletar_veiculo"),
    path('solicitar-manutencao/<int:veiculo_id>/', views.solicitar_manutencao, name='solicitar_manutencao'),
    path('criar-manutencao/<int:veiculo_id>/', views.criar_manutencao_veiculo, name='criar_manutencao_veiculo'),
]