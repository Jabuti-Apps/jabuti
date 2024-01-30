from django.db import models

class Motorista(models.Model):

    nome = models.TextField()

    cnh = models.TextField()

class Carro(models.Model):

    marca = models.TextField()

    modelo = models.TextField()

    ano = models.IntegerField()

    vin = models.TextField()

    proprietario = models.ForeignKey("Motorista", on_delete=models.SET_NULL, null=True)