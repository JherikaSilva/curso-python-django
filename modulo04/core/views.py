from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context={
        'nome_usuario':'Jherika',
        'tecnologias': ['Python', 'Django', 'HTML','CSS']
    }
    
    return render(request, 'home.html', context)


def ola(request):
    
    return HttpResponse("<h1>Bem vindo!</h1><p><input>LOGIN</input><br></h1><input>SENHA</input></p>")
    