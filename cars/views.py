from django.shortcuts import render, get_object_or_404
from cars.models import Veiculo
from manutencao.models import Manutencao

def cars(request):
    veiculos = Veiculo.objects.all().order_by('id')
    return render(request, "index.html", {"veiculos": veiculos})

def car_detail(request, id):
    car_obj = get_object_or_404(Veiculo, id=id)
    manutencao_obj = Manutencao.objects.filter(veiculo=car_obj).order_by('-data')

    context = {
        "veiculo": car_obj,
        "manutencoes": manutencao_obj,
    }
    return render(request, "car_detail.html", context)

def disponiveis(request):
    veiculos_disponiveis = Veiculo.objects.filter(estaDisponivel=True)
    return render(request, 'index.html', {'veiculos': veiculos_disponiveis})

