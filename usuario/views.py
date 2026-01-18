from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout,login,authenticate
from .forms import cadastrarform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def logout_usuario(request):
    #fazer logout
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def cadastrar(request):
    #fazer cadastro usuario
    if request.method != 'POST':

        form = cadastrarform()

    else:
        
        form = cadastrarform(request.POST)

        if form.is_valid():
            novo_usuario = form.save()
            #verificar o usuario no banco de dados
            authenticated_user = authenticate(username =  novo_usuario.username, password = request.POST['password1'] )
            #logar o usuario automaticamente para entrar 
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))

    return render(request, "usuario/cadastrar.html", {"form": form})
