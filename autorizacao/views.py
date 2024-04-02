from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, "signup.html")

def logout_user(request):
    logout(request)
    return redirect("/")

def criar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = User.objects.create_user(username, email, password)
        user.save()

        if user is not None:
            
            return redirect("/")
        else:
            return render(request, "nao_autorizado.html")

    return render(request, "nao_autorizado.html")


def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect("/veiculos")
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect("/")

def calendar(request):
    return render(request, 'calendar.html')
