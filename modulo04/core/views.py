from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Tarefa
from .forms import TarefaForm 

def home(request):

    if request.method== 'POST':
        
        form= TarefaForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('home')
    
    else:
        
        form=TarefaForm()


    
    todas_as_tarefas=Tarefa.objects.all().order_by('-criada_em')

    context={
        'nome_usuario':'Jherika',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS','Models','Admin'],
        'tarefas': todas_as_tarefas,
        'form': form,
    }
    
    return render(request, 'home.html', context)


def ola(request):
    
    return HttpResponse("<h1>Bem vindo!</h1><p><input>LOGIN</input><br></h1><input>SENHA</input></p>")
    