from django.forms import ModelForm
from .models import Tarefa, Usuario


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome_tarefa', 'dia', 'descricao', 'categoria', 'status']


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_usuario', 'email', 'senha']