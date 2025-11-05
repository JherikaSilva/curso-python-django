from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")

def ola(request):
    
    return HttpResponse("<h1>Bem vindo!</h1><p><input>LOGIN</input><br></h1><input>SENHA</input></p>")
    