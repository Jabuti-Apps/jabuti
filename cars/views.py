from django.shortcuts import render

from cars.models import Carro, Motorista



def car_detail(request, pk):

    owner_obj = Motorista.objects.get(pk=pk)

    car_objs = Carro.objects.filter(proprietario_id=owner_obj.id)

    context = {

        "vehicles": car_objs,

        "drivers": owner_obj,

    }

    return render(request, "car_detail.html", context)