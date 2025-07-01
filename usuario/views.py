from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login

def new_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autentica e loga o usuário após cadastro
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/usuario.html', {'form': form})