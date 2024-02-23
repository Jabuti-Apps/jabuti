from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def autorizacao(request):
    return render(request, "index.html")

# def criar(request, user):

def login(request, username, password):
    user = authenticate(username=username, password=password)

    if user is not None:
        return redirect("disponiveis")
    else:
        return render(request, "nao_autorizado.html")

