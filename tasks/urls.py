from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home, tarefa, nova_tarefa, delete, filtrar, UsuarioCreate


urlpatterns = [
    path('', home, name='home'),
    path('tarefa/<int:pk>', tarefa, name='tarefa'),
    path('delete/<int:pk>', delete, name='delete'),
    path('filtro/<str:pk>', filtrar, name='filtro'),
    path('nova', nova_tarefa, name='nova'),
    path('cadastro', UsuarioCreate.as_view(), name='cadastro'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="registration/redefinir_senha.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/enviado.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/nova_senha.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/redefinido.html"),
         name="password_reset_complete"),
]







