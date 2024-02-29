from datetime import timezone
from django.db import models

from veiculos.models import Veiculo

class Manutencao(models.Model):

    OPCOES_MANUTENCAO = [
        ('Troca de Oleo', 'Troca de Oleo'),
        ('Troca de Pneu', 'Troca de Pneu'),
        ('Troca Kit de Freio', 'Troca Kit de Freio'),
        ('Limpeza do radiador', 'Limpeza do radiador'),
        ('Outro', 'Outro'),
    ]

    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    tipoManutencao = models.CharField(max_length=100, choices=OPCOES_MANUTENCAO, default=None)
    outraOpcao = models.CharField(max_length=100, blank=True, null=True)
    quilometragemDoVeiculo = models.FloatField()
    dataEntrada = models.DateField(blank=True, null=True)
    dataSaida = models.DateField(blank=True, null=True)
    criadoEm = models.DateTimeField(auto_now_add=True)