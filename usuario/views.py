from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout,login,authenticate
from .forms import cadastrarform


def logout_usuario(request):
    #fazer logout
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def cadastrar(request):
    #fazer cadastro usuario
    if request.method == 'POST':
        form = cadastrarform(dados = request.POST)

        if form.is_valid():
            novo_usuario = form.save()
            #verificar o usuario no banco de dados
            authenticated_user = authenticate(nome_usuario =  novo_usuario.nome_usuario, password = request.POST['password'] )
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
        
    else:
        form = cadastrarform()

    context = {"form": form}

    return render(request, "usuário/cadastrar.html", context)
