from django.shortcuts import render, redirect
from .form import TarefaForm
from .models import Tarefa
import datetime
# Create your views here. Funções que serão chamadas nas rotas


def home(request):
    tarefas = Tarefa.objects.all()

    context = {
        'tarefas': tarefas,
    }

    return render(request, 'home.html', context)


def tarefa(request, pk):
    tarf = Tarefa.objects.get(id=pk)
    form = TarefaForm(request.POST or None, instance=tarf)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'tarefa': form,
    }

    return render(request, 'tarefa.html', context)


def nova_tarefa(request):
    data = {}
    form = TarefaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    data['form'] = form
    return render(request, 'nova.html', data)



