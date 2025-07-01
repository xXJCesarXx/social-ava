from django.urls import path
from django.contrib.auth import views as auth_views
from .views import new_usuario

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuario/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='social/index.html',
        next_page='login'
    ), name='logout'),
    path('new_usuario/', new_usuario, name='new_usuario'),
    path('registrar/', new_usuario, name='registrar'),  # Adicione esta linha para o link do template
]