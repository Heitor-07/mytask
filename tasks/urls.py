from django.urls import path

from .views import home, tarefa, nova_tarefa

urlpatterns = [
    path('', home, name='home'),
    path('tarefa/<int:pk>', tarefa, name='tarefa'),
    path('nova', nova_tarefa, name='nova'),
]

