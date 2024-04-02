from django.db import models
    
class Agendamento(models.Model):

    veiculo = models.ForeignKey('veiculos.Veiculo', on_delete=models.DO_NOTHING, null = False, blank = False )
    Origem = models.CharField(max_length=50, null = False, blank = False)
    Destino = models.CharField(max_length=50, null = False, blank = False)
    HorariodeEntrada = models.DateTimeField(null= False, blank = False, default="")
    HorariodeSaida = models.DateTimeField(null= True, blank = True)
    quilometragemFinal = models.IntegerField(null= True, blank = True)
    quilometragemInicial= models.IntegerField(null= True, blank = True)
    finalizado = models.BooleanField(default=False)
    motivo = models.TextField(default="")




    def __str__(self):
        return f'Origem: {self.Origem}, Destino: {self.Destino}, HorariodeEntrada: {self.HorariodeEntrada}, HorariodeSaida: {self.HorariodeSaida} '
