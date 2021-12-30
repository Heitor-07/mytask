from django.contrib import admin

# Register your models here.

from .models import Tarefa, Usuario, Categoria


class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome_tarefa', 'dia', 'descricao', 'categoria')


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_usuario', 'email', 'senha')


admin.site.register(Categoria)
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Usuario, UsuarioAdmin)




