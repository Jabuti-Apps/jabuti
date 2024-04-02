from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from veiculos.models import Veiculo
from .models import Abastecer

def abastecimentos(request):
    abastecimentos = Abastecer.objects.all()
    return render(request, "abastecimento.html", {"abastecimentos": abastecimentos})

def criar_abastecimento(request):
    if request.method == 'GET':
        veiculo = Veiculo.objects.all()
        abastecimento = Abastecer.objects.all()

        veiculo_filtrar = request.GET.get('veiculo')

        if veiculo_filtrar:
            veiculo = veiculo.filter(veiculo_id=veiculo_filtrar)

        return render(
            request,
            'abastecer.html',
            {
                'veiculos': veiculo,
                'abastecimentos': abastecimento,
            }
            
        )
    
    elif request.method == 'POST':
        veiculo = request.POST.get('veiculo')
        valorpago = request.POST.get('valorpago')


        abastecimento = Abastecer(
            veiculo_id=veiculo,
            valorpago=valorpago
        )


        abastecimento.save()

        return redirect('/abastecimento/')
    
def deletar_abastecimento(request, abastecimento_id):
    
    abastecer = Abastecer.objects.get(id=abastecimento_id)
    abastecer.delete()
    return redirect("/abastecimento/")
