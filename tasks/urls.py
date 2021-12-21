from django.urls import path

from .views import home, tarefa

urlpatterns = [
    path('', home, name='home'),
    path('tarefa/<int:pk>', tarefa, name='tarefa'),
]

