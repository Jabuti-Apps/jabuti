from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from autorizacao.decorators import gestor_required
from .models import CustomUser, Orgao
from veiculos.models import Veiculo
from manutencao.models import Manutencao
from agendamento.models import Agendamento
from abastecimento.models import Abastecer
from django.core.paginator import Paginator
from django.db.models import Count

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, "signup.html")

@login_required
def logout_user(request):
    logout(request)
    return redirect("/")

@gestor_required
def cadastro(request):
    if request.method == "GET":
        role_choices = CustomUser.ROLE_CHOICES
        orgaos = Orgao.objects.all()

        return render(request, 'cadastro.html', {'role_choices': role_choices, 'orgaos': orgaos})

    
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")
        cnh = request.POST.get("cnh")
        foto = request.FILES.get('foto')
        orgao_id = request.POST.get('orgao')  


        orgao = Orgao.objects.get(pk=orgao_id)

        

        CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
            orgao=orgao,
            cnh=cnh,
            foto=foto,
        )

        return redirect("funcionarios")


def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/calendar")
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect("/")

def calendar(request):
    return render(request, 'calendar.html')

@gestor_required
def funcionarios(request):
    if request.method == 'GET':
        usuarios = CustomUser.objects.all().order_by('username')

        # Configuração da paginação
        paginator = Paginator(usuarios, 10)  # Exibir 5 objetos por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'funcionarios.html', {'usuarios':usuarios, 'page_obj': page_obj})
    
@gestor_required
def gerenciar_funcionario(request, funcionario_id):
    funcionario = CustomUser.objects.get(id=funcionario_id)
    
    if request.method == "POST":
        if "ativar" in request.POST:
            funcionario.is_active = True
            funcionario.save()
        elif "desativar" in request.POST:
            funcionario.is_active = False
            funcionario.save()

        return redirect('funcionarios') 
    
def dashboard(request):
    orgao=request.user.orgao
    veiculos = Veiculo.objects.filter(orgao=request.user.orgao)
    agendamentos = Agendamento.objects.filter(veiculo__orgao = orgao)
    manutencoes = Manutencao.objects.filter(veiculo__orgao = orgao)
    abastecimentos = Abastecer.objects.filter(veiculo__orgao = orgao)


    quantidade_veiculos = [veiculos.count()]
    quantidade_agendamentos = [agendamentos.count()]
    quantidade_manutencoes = [manutencoes.count()]
    quantidade_abastecimentos = [abastecimentos.count()]

    return render(request, 'dashboard.html', {
        'quantidade_veiculos': quantidade_veiculos,
        'quantidade_agendamentos': quantidade_agendamentos,
        'quantidade_manutencoes': quantidade_manutencoes,
        'quantidade_abastecimentos': quantidade_abastecimentos,
        'orgao':orgao,
    })