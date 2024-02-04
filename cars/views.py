from django.shortcuts import render, get_object_or_404

from cars.models import Veiculo

def cars(request):
    veiculos = Veiculo.objects.all()
    return render(request, "index.html", {"veiculos": veiculos})

def car_detail(request, pk):
    car_objs = get_object_or_404(Veiculo, pk=pk)

    context = {
        "veiculo": car_objs,
    }
    return render(request, "car_detail.html", context)