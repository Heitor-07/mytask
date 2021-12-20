from django.shortcuts import render
from .models import Tarefa
# Create your views here. Funções que serão chamadas nas rotas


def home(request):
    tarefas = Tarefa.objects.all()

    context = {
        'tarefas': tarefas,
    }

    return render(request, 'home.html', context)




