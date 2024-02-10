from django.urls import path
from . import views

urlpatterns = [

    path('', views.manutencao),
    path('criar-manutencao/', views.criar_manutencao, name='criar_manutencao'),
]