from django.forms import ModelForm
from .models import Tarefa
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome_tarefa', 'dia', 'descricao', 'categoria', 'status']


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email']