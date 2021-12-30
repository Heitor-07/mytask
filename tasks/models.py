import datetime

from django.db import models
from datetime import datetime

# Create your models here. Classes que vão para o banco de dados
from django.db.models import DateField


class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=50)

    def __str__(self):
        return self.categoria


STATUS_CHOICES = (
    ("Pendente", "Pendente"),
    ("Concluída", "Concluída"),
    ("Adiada", "Adiada"),
)


class Tarefa(models.Model):
    nome_tarefa = models.CharField('Tarefa', max_length=100)
    dia = models.DateField('Dia')
    descricao = models.CharField('Descrição', max_length=500)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Pendente")

    def __str__(self):
        return self.nome_tarefa


class Usuario(models.Model):
    nome_usuario = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    senha = models.CharField('Senha', max_length=16)

    def __str__(self):
        return self.nome_usuario


