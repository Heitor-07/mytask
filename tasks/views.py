from django.shortcuts import render, redirect
from .form import TarefaForm
from django.contrib.auth.decorators import login_required
from .models import Tarefa, Categoria

# Create your views here. Funções que serão chamadas nas rotas


@login_required
def home(request):
    tarefas = Tarefa.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'tarefas': tarefas,
        'categoria': categorias,
    }

    return render(request, 'home.html', context)


@login_required
def filtrar(request, pk):
    filtros = Tarefa.objects.filter(categoria=pk)
    categorias = Categoria.objects.all()

    context = {
        'filtre': filtros,
        'categoria': categorias,
    }

    return render(request, 'filtro.html', context)


@login_required
def tarefa(request, pk):
    tarf = Tarefa.objects.get(id=pk)
    forms = TarefaForm(request.POST or None, instance=tarf)

    if forms.is_valid():
        forms.save()
        return redirect('home')

    context = {
        'tarefa': forms,
        'del_tarefa': tarf,
    }

    return render(request, 'tarefa.html', context)


@login_required
def delete(request, pk):
    del_tarefa = Tarefa.objects.get(id=pk)
    del_tarefa.delete()
    return redirect('home')


@login_required
def nova_tarefa(request):
    data = {}
    forms = TarefaForm(request.POST or None)

    if forms.is_valid():
        forms.save()
        return redirect('home')

    data['form'] = forms
    return render(request, 'nova.html', data)


