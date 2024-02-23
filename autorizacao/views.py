from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def autorizacao(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

@csrf_exempt
def criar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = User.objects.create_user(username, email, password)
        user.save()

        if user is not None:
            return redirect("disponiveis")
        else:
            return render(request, "nao_autorizado.html")

    return render(request, "nao_autorizado.html")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(username=username, password=password)

        if user is not None:
            return redirect("disponiveis")
        else:
            return render(request, "nao_autorizado.html")

    return render(request, "nao_autorizado.html")

