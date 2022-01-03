from django.contrib import admin

# Register your models here.

from .models import Tarefa, Categoria


class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome_tarefa', 'dia', 'descricao', 'categoria', 'usuario')


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_usuario', 'email', 'senha')


admin.site.register(Categoria)
admin.site.register(Tarefa, TarefaAdmin)





