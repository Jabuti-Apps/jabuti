from django.db import models

class Veiculo(models.Model):

    OPCOES_GASOLINA = [
        ('Gasolina', 'Gasolina'),
        ('Gasolina/Alcool', 'Gasolina/Alcool'),
        ('Diesel', 'Diesel'),
        ('DieselS10', 'DieselS10'),
        ('Etanol', 'Etanol'),
    ]

    crv = models.BigIntegerField()
    cor = models.TextField()
    placa = models.TextField(max_length=7)
    marca = models.TextField()
    modelo = models.TextField()
    anoDeFabricacao = models.IntegerField()
    tipoDeCombustivel = models.CharField(max_length=100, choices=OPCOES_GASOLINA, default=None)
    capacidadeCombustivel = models.IntegerField()
    quilometragem = models.FloatField()
    estaDisponivel = models.BooleanField(default=True)
    precisaAbastecer = models.BooleanField(default=False)
    precisaDeManutencao = models.BooleanField(default=False)
    temSeguro  = models.BooleanField(default=None)
    alugado  = models.BooleanField(default=None)
    #orgao int [ref: > orgao.id]
    ultimaLavagem = models.DateField(default=None, blank=True, null=True)
    criadoEm = models.DateTimeField(auto_now_add=True)