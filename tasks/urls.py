from django.urls import path

from .views import home, tarefa, nova_tarefa, delete

urlpatterns = [
    path('', home, name='home'),
    path('tarefa/<int:pk>', tarefa, name='tarefa'),
    path('delete/<int:pk>', delete, name='delete'),
    path('nova', nova_tarefa, name='nova'),
]

