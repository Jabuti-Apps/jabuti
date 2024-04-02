from django.urls import path
from . import views

urlpatterns = [

    path('', views.abastecimentos, name="abastecer"),
    path('criar_abastecimento', views.criar_abastecimento, name="criar_abastecer" ),
    path('deletar_abastecimento/<int:agendamento_id>/', views.deletar_abastecimento, name='deletar_abastecimento'),
]