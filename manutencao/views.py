from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from autorizacao.decorators import gestor_required
from manutencao.models import Manutencao
from veiculos.models import Veiculo

@gestor_required
def manutencao(request):
    orgao=request.user.orgao
    manutencoes = Manutencao.objects.filter(veiculo__orgao = orgao)
    hoje = date.today() 
    context = {
        'manutencoes': manutencoes,
        'hoje': hoje, 
    }
    return render(request, "manutencao.html", context)

@gestor_required
def criar_manutencao(request):
    veiculos_manutencao = Veiculo.objects.filter(precisaDeManutencao=True).filter(orgao=request.user.orgao)

    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo')
        tipo_manutencao = request.POST.get('tipo_manutencao')
        outra_opcao = request.POST.get('outra_opcao', '') 
        quilometragem = request.POST.get('quilometragem')
        dataEntrada = request.POST.get('dataEntrada')
        dataSaida = request.POST.get('dataSaida')
        
        Manutencao.objects.create(
            veiculo_id=veiculo_id,
            tipoManutencao=tipo_manutencao,
            outraOpcao=outra_opcao,
            quilometragemDoVeiculo=quilometragem,
            dataEntrada=dataEntrada,
            dataSaida=dataSaida
        )

        # Adiciona uma mensagem de sucesso
        messages.add_message(request, constants.SUCCESS, 'Manutenção cadastrada com sucesso.')

        # Redireciona de volta para a página de criação de manutenção
        return redirect('manutencao')

    return render(request, 'criar_manutencao.html', {"veiculos": veiculos_manutencao})

@gestor_required
def update_manutencao(request, manutencao_id):
    manutencao = get_object_or_404(Manutencao, id=manutencao_id)

    manutencao.dataEntrada = manutencao.dataEntrada.strftime('%Y-%m-%d')
    manutencao.dataSaida = manutencao.dataSaida.strftime('%Y-%m-%d')

    if request.method == 'POST':
        manutencao.veiculo.placa = request.POST.get('veiculo')
        manutencao.tipoManutencao = request.POST.get('tipo_manutencao')
        manutencao.outraOpcao = request.POST.get('outra_opcao', '')
        manutencao.quilometragemDoVeiculo = request.POST.get('quilometragem')
        manutencao.dataEntrada = request.POST.get('dataEntrada')
        manutencao.dataSaida = request.POST.get('dataSaida')


        manutencao.save()
        return redirect('manutencao')

    return render(request, 'update_manutencao.html', {"manutencao":manutencao})

@gestor_required
def deletar_manutencao(request, manutencao_id):
    manutencao = Manutencao.objects.get(id=manutencao_id)
    manutencao.delete()
    return redirect('manutencao')