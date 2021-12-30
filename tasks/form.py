from django.forms import ModelForm
from .models import Tarefa


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome_tarefa', 'dia', 'descricao', 'categoria', 'status']