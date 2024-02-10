from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from manutencao.models import Manutencao
from veiculos.models import Veiculo

def manutencao(request):
    manutencoes = Manutencao.objects.all()
    return render(request, "manutencao.html", {"manutencoes": manutencoes})

def criar_manutencao(request):
    veiculos_manutencao = Veiculo.objects.filter(precisaDeManutencao=True)

    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo')
        tipo_manutencao = request.POST.get('tipo_manutencao')
        outra_opcao = request.POST.get('outra_opcao', '') 
        quilometragem = request.POST.get('quilometragem')
        data = request.POST.get('data')
        
        Manutencao.objects.create(
            veiculo_id=veiculo_id,
            tipoManutencao=tipo_manutencao,
            outraOpcao=outra_opcao,
            quilometragemDoVeiculo=quilometragem,
            data=data
        )

        # Após criar a manutenção, altera a coluna precisaDeManutencao para False no veículo correspondente
        veiculo = Veiculo.objects.get(id=veiculo_id)
        veiculo.precisaDeManutencao = False
        veiculo.save()

        # Adiciona uma mensagem de sucesso
        messages.success(request, 'Manutenção criada com sucesso.')

        # Redireciona de volta para a página de criação de manutenção
        return redirect('criar_manutencao')

    return render(request, 'criar_manutencao.html', {"veiculos": veiculos_manutencao})
