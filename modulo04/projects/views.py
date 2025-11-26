from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

@login_required
def adicionar_projeto(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            projeto= form.save(commit=False)
            projeto.user= request.user
            projeto.save()
            messages.success(request, "Projeto criado com sucesso!", extra_tags="concluida")
            return redirect("home")
    else:
        form = ProjectForm()

    return render(request, "adicionar_projeto.html", {"form": form})
