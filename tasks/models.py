
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here. Classes que vão para o banco de dados
from django.views.generic import CreateView


CATEGORIA_CHOICES = (
    ("Casa", "Casa"),
    ("Trabalho", "Trabalho"),
    ("Escola", "Escola"),
    ("Contas", "Contas"),
)


class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=50, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.categoria


STATUS_CHOICES = (
    ("Pendente", "Pendente"),
    ("Concluída", "Concluída"),
    ("Adiada", "Adiada"),
)


class Tarefa(models.Model, LoginRequiredMixin, CreateView):
    nome_tarefa = models.CharField('Tarefa', max_length=100)
    dia = models.DateTimeField('Dia')
    descricao = models.TextField('Descrição', max_length=500)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Pendente")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_tarefa


