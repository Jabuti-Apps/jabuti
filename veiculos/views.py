from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from autorizacao.decorators import gestor_required
from veiculos.models import Veiculo
from manutencao.models import Manutencao
from autorizacao.models import Orgao
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@gestor_required
def veiculos(request):
    veiculos = Veiculo.objects.filter(orgao=request.user.orgao).order_by('id')
    # Configuração da paginação
    paginator = Paginator(veiculos, 5)  # Exibir 5 veículos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,"veiculos.html", {'page_obj': page_obj})

@gestor_required
def detalhe_veiculo(request, veiculo_id):
    car_obj = get_object_or_404(Veiculo, id=veiculo_id)
    manutencao_obj = Manutencao.objects.filter(veiculo=car_obj).order_by('-dataEntrada')

    context = {
        "veiculo": car_obj,
        "manutencoes": manutencao_obj,
    }
    return render(request, "detalhe_veiculo.html", context)

@gestor_required
def cadastrar_veiculo(request):
    if request.method == 'GET':
        opcoes_gasolina = Veiculo.OPCOES_GASOLINA
        orgaos = Orgao.objects.all()
        return render(request, 'cadastrar_veiculo.html', {'orgaos': orgaos, 'opcoes_gasolina': opcoes_gasolina})


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
        orgao_id = request.POST.get('orgao')

        orgao = Orgao.objects.get(pk=orgao_id)

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
            alugado=alugado,
            orgao=orgao,
        )

        return redirect('veiculos')
    
    return render(request, 'cadastrar_veiculo.html')

@gestor_required
def update_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    
    if request.method == 'POST':
        veiculo.crv = request.POST.get('crv')
        veiculo.marca = request.POST.get('marca')
        veiculo.modelo = request.POST.get('modelo') 
        veiculo.cor = request.POST.get('cor')
        veiculo.placa = request.POST.get('placa')
        veiculo.anoDeFabricacao = request.POST.get('anoDeFabricacao')
        veiculo.capacidadeCombustivel = request.POST.get('capacidadeCombustivel')
        veiculo.tipoDeCombustivel = request.POST.get('tipoDeCombustivel')
        veiculo.quilometragem = request.POST.get('quilometragem')
        veiculo.temSeguro = request.POST.get('temSeguro')
        veiculo.alugado = request.POST.get('alugado')

        veiculo.save()
        messages.success(request, 'Veículo atualizado com sucesso.')
        return redirect('veiculos')

    return render(request, 'update_veiculo.html', {"veiculo": veiculo})

@gestor_required
def deletar_veiculo(request, veiculo_id):
    veiculo = Veiculo.objects.get(id=veiculo_id)
    veiculo.delete()
    return redirect('veiculos')

@gestor_required
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

@gestor_required
def criar_manutencao_veiculo(request, veiculo_id):
    if request.method == 'POST':
        tipo_manutencao = request.POST.get('tipo_manutencao')
        outra_opcao = request.POST.get('outra_opcao', '') 
        quilometragem = request.POST.get('quilometragem')
        dataEntrada = request.POST.get('data')
        dataSaida = request.POST.get('data')

        Manutencao.objects.create(
            veiculo_id=veiculo_id,
            tipoManutencao=tipo_manutencao,
            outraOpcao=outra_opcao,
            quilometragemDoVeiculo=quilometragem,
            dataEntrada=dataEntrada,
            dataSaida=dataSaida
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