from django.db import models

from veiculos.models import Veiculo

class Abastecer(models.Model):

  veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
  valorpago = models.FloatField(null=False, blank = False)