from django.shortcuts import render
from django.http import HttpResponse
from.models import Tarefa

def home(request):
    
    todas_as_tarefas=Tarefa.objects.all()

    context={
        'nome_usuario':'Jherika',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS','Models','Admin'],
        'tarefas': todas_as_tarefas
    }
    
    return render(request, 'home.html', context)


def ola(request):
    
    return HttpResponse("<h1>Bem vindo!</h1><p><input>LOGIN</input><br></h1><input>SENHA</input></p>")
    