from django.shortcuts import get_object_or_404, render,redirect


from .models import Agendamento
from veiculos.models import Veiculo
from django.contrib.auth.decorators import login_required

@login_required(login_url='/autorizacao/')
def criar_agendamento(request):

    if request.method == 'GET':
        veiculo = Veiculo.objects.all()
        agendamento = Agendamento.objects.all()

        veiculo_filtrar = request.GET.get('veiculo')

        if veiculo_filtrar:
            veiculo = veiculo.filter(veiculo_id=veiculo_filtrar)

        return render(
            request,
            'agendamento.html',
            {
                'veiculos': veiculo,
                'agendamentos': agendamento,
            }
            
        )
    
    elif request.method == 'POST':
        origem = request.POST.get('origem')
        destino = request.POST.get('destino')
        veiculo = request.POST.get('veiculo')
        horariodeentrada = request.POST.get('horaiodeentrada')
        motivosaida = request.POST.get('motivo')


        agendamento = Agendamento(
            Origem=origem,
            Destino=destino,
            veiculo_id=veiculo,
            HorariodeEntrada=horariodeentrada,
            motivo = motivosaida,
        )


        agendamento.save()

        return redirect('/agendamento/')

@login_required(login_url='/autorizacao/')
def agendamentos(request):

    veiculo = Veiculo.objects.all()
    agendamento = Agendamento.objects.all()
    veiculo_filtrar = request.GET.get('veiculo')

    ##Filtro para os horarios de agendamento - não pode marcar em uma data anterior a de agora 
    ##Realizar filtro para fica amostra se o agendamento foi finalizado ou não

    if veiculo_filtrar:
        veiculo = veiculo.filter(veiculo_id=veiculo_filtrar)
    else:
        agendamento = Agendamento.objects.filter(finalizado = False).order_by('id')
    return render(request, "listar_agendamento.html", {"veiculos": veiculo, 'agendamento': agendamento})

@login_required(login_url='/autorizacao/')
def deletar_agendamento(request, agendamento_id):

    agendamento = Agendamento.objects.get(id=agendamento_id)
    agendamento.delete()
    return redirect("agendamentos")

@login_required(login_url='/autorizacao/')
def finalizar_agendamento(request, agendamento_id):

    agendamento = Agendamento.objects.get(id=agendamento_id)

    if request.method == 'POST':
        horariodesaida = request.POST.get('horaiodesaida')

        #if horariodesaida < agendamento.HorariodeSaida:
            #return redirect('/agendamento/finalizar_agendamento/{{agendamento.}}') tratamento
        

        agendamento.HorariodeSaida = horariodesaida

        if agendamento.HorariodeSaida != None :
            agendamento.finalizado = True

        agendamento.save()

        return redirect('/agendamento/')
        

    return render(
            request,
            'finalizar_agendamento.html',
            {
                'agendamento': agendamento,
            }
            
        )

def detalhe_agendamento(request, agendamento_id):
    agendamento_obj = get_object_or_404(Agendamento, id=agendamento_id)
    veiculo = Veiculo.objects.all()

    context = {
        "agendamento": agendamento_obj, 
        "veiculos": veiculo,
    }
    return render(request, "detalhe_agendamento.html", context)