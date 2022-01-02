from django.urls import path

from .views import home, tarefa, nova_tarefa, delete, filtrar, UsuarioCreate


urlpatterns = [
    path('', home, name='home'),
    path('tarefa/<int:pk>', tarefa, name='tarefa'),
    path('delete/<int:pk>', delete, name='delete'),
    path('filtro/<str:pk>', filtrar, name='filtro'),
    path('nova', nova_tarefa, name='nova'),
    path('cadastro', UsuarioCreate.as_view(), name='cadastro'),
]

