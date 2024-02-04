from django.db import models

class Veiculo(models.Model):

    crv = models.BigIntegerField()

    cor = models.TextField()

    placa = models.TextField()

    marca = models.TextField()

    modelo = models.TextField()

    anoDeFabricacao = models.IntegerField()

    tipoDeCombustivel = models.TextField()

    capacidadeCombustivel = models.IntegerField()

    quilometragem = models.FloatField()

    estaDisponivel = models.BooleanField(default=True)

    precisaAbastecer = models.BooleanField(default=False)

    precisaDeManutencao = models.BooleanField(default=False)

    temSeguro  = models.BooleanField(default=False)

    alugado  = models.BooleanField(default=False)

    #orgao int [ref: > orgao.id]

    criadoEm = models.DateTimeField(auto_now_add=True)