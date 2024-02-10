from django.db import models

from veiculos.models import Veiculo  # Importa o modelo Veiculo do aplicativo veiculos

class Manutencao(models.Model):

  OPCOES_MANUTENCAO = [
    ('Troca de Oleo', 'Troca de Oleo'),
    ('Troca de Pneu', 'Troca de Pneu'),
    ('Troca Kit de Freio', 'Troca Kit de Freio'),
    ('Limpeza do radiador', 'Limpeza do radiador'),
    ('Outro', 'Outro'),  # Opção para o usuário digitar uma nova opção
  ]

  veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
  tipoManutencao = models.CharField(max_length=100, choices=OPCOES_MANUTENCAO, default=None)
  outraOpcao = models.CharField(max_length=100, blank=True, null=True)  # Campo para armazenar a nova opção digitada pelo usuário
  quilometragemDoVeiculo = models.FloatField()
  data = models.DateField()
  criadoEm = models.DateTimeField(auto_now_add=True)