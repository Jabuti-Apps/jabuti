from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from veiculos.models import Veiculo
from manutencao.models import Manutencao

def veiculos(request):
    veiculos = Veiculo.objects.all().order_by('id')
    
    return render(request,"index.html", {"veiculos": veiculos,})

def detalhe_veiculo(request, veiculo_id):
    car_obj = get_object_or_404(Veiculo, id=veiculo_id)
    manutencao_obj = Manutencao.objects.filter(veiculo=car_obj).order_by('-data')

    context = {
        "veiculo": car_obj,
        "manutencoes": manutencao_obj,
    }
    return render(request, "detalhe_veiculo.html", context)

def cadastrar_veiculo(request):
    if request.method == 'POST':
        crv = request.POST.get('crv')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo') 
        cor = request.POST.get('cor')
        placa = request.POST.get('placa')
        anoDeFabricacao = request.POST.get('anoDeFabricacao')
        capacidadeCombustivel = request.POST.get('capacidadeCombustivel')
        tipoDeCombustivel = request.POST.get('tipoDeCombustivel')
        quilometragem = request.POST.get('quilometragem')
        temSeguro = request.POST.get('temSeguro')
        alugado = request.POST.get('alugado')

        Veiculo.objects.create(
            crv=crv,
            marca = marca,
            modelo =modelo,
            cor=cor,
            placa=placa,
            anoDeFabricacao=anoDeFabricacao,
            capacidadeCombustivel= capacidadeCombustivel,
            tipoDeCombustivel=tipoDeCombustivel,
            quilometragem=quilometragem,
            temSeguro=temSeguro,
            alugado=alugado
        )

        return redirect('veiculos')
    
    return render(request, 'cadastrar_veiculo.html')

def editar_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    return render(request, 'forms.html', {"veiculo":veiculo})

def update_veiculo(request, veiculo_id):
    if request.method == 'POST':
        vcrv = request.POST.get('crv')
        vmarca = request.POST.get('marca')
        vmodelo = request.POST.get('modelo') 
        vcor = request.POST.get('cor')
        vplaca = request.POST.get('placa')
        vanoDeFabricacao = request.POST.get('anoDeFabricacao')
        vcapacidadeCombustivel = request.POST.get('capacidadeCombustivel')
        vtipoDeCombustivel = request.POST.get('tipoDeCombustivel')
        vquilometragem = request.POST.get('quilometragem')
        vtemSeguro = request.POST.get('temSeguro')
        valugado = request.POST.get('alugado')

    veiculo = Veiculo.objects.get(id=veiculo_id)
    
    veiculo.crv = vcrv
    veiculo.marca = vmarca
    veiculo.modelo = vmodelo
    veiculo.cor = vcor
    veiculo.placa = vplaca
    veiculo.anoDeFabricacao = vanoDeFabricacao
    veiculo.capacidadeCombustivel = vcapacidadeCombustivel
    veiculo.tipoDeCombustivel = vtipoDeCombustivel
    veiculo.quilometragem = vquilometragem
    veiculo.temSeguro = vtemSeguro
    veiculo.alugado = valugado

    veiculo.save()
    return redirect('veiculos')

def deletar_veiculo(request, veiculo_id):
    veiculo = Veiculo.objects.get(id=veiculo_id)
    veiculo.delete()
    return redirect('veiculos')

def solicitar_manutencao(request, veiculo_id):
    if request.method == 'POST':
        veiculo = Veiculo.objects.get(id=veiculo_id)
        
        # Verifique se há uma manutenção agendada para o veículo no dia atual ou nos próximos dias
        data_atual = timezone.now().date()
        proximos_dias = data_atual + timezone.timedelta(days=30)  # Verifique para os próximos 30 dias
        manutencao_existente = Manutencao.objects.filter(
            veiculo=veiculo,
            data__range=[data_atual, proximos_dias]
        ).exists()
        
        if manutencao_existente:
            # Se uma manutenção já existir, retorne uma resposta de erro
            messages.error(request, 'Já existe uma manutenção agendada para o veículo no dia atual ou nos próximos dias.')
            return redirect('detalhe_veiculo', veiculo_id=veiculo_id)
        
        # Se não houver uma manutenção agendada, proceda com a solicitação de manutenção
        veiculo.precisaDeManutencao = True
        veiculo.estaDisponivel = False
        veiculo.save()

        # Implementar logica da tabela de alerta !!! -------------------------------------

        return redirect('detalhe_veiculo', veiculo_id=veiculo_id)



def criar_manutencao_veiculo(request, veiculo_id):
    if request.method == 'POST':
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
        return redirect('criar_manutencao_veiculo', veiculo_id)

    return render(request, 'criar_manutencao_veiculo.html',)