from django.shortcuts import render, get_object_or_404
from manutencao.models import Manutencao

def manutencao(request):
    manutencoes = Manutencao.objects.all()
    
    return render(request, "manutencao.html", {"manutencoes": manutencoes})
