from django.contrib.auth.models import AbstractUser
from django.db import models

class Orgao(models.Model):
    orgao = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.orgao

class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('M', 'Motorista'),
        ('G', 'Gestor'),
        ('F', 'Funcionário'),
    ]

    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='G')
    foto = models.ImageField(upload_to="fotos_perfil", null=True, blank=True)
    cnh = models.CharField(max_length=11, null=True, blank=True)
    orgao = models.ForeignKey(Orgao, on_delete=models.DO_NOTHING, null=True, blank=True)

    def get_foto_perfil(self):
        return self.foto.url if self.foto else None