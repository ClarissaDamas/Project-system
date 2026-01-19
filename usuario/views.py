from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from .forms import cadastrarform
from django.shortcuts import render,get_object_or_404,redirect
from .models import Usuario


#Logout do usuario.
def logout_usuario(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))

#Cadastro do usuario.
def cadastrar(request):
   
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

def perfil(request, user_id):
    #perfil = get_object_or_404(Usuario, id = user_id)
    #perfil = usuario.subitens.all().order_by('-id')
    #if usuario.username == request.user: 
    return render(request, 'usuario/perfil.html', {'perfil':perfil} )
    #else:
        #return render(request, 'System/error.html' )
    
