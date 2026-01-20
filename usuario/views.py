from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from .forms import cadastrarform


#Logout do usuário.
def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



#Cadastro do usuário.
def cadastrar(request):

    if request.method != 'POST':
        form = cadastrarform()

    else:    
        form = cadastrarform(request.POST)

        if form.is_valid():
            novo_usuario = form.save()
            #Verificar o usuário no banco de dados.
            authenticated_user = authenticate(username =  novo_usuario.username, password = request.POST['password1'] )
            #Logar o usuário automaticamente. 
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))

    return render(request, "usuario/cadastrar.html", {"form": form})


#Perfil do usuário
def perfil(request, user_id):
    return render(request, 'usuario/perfil.html', {'perfil':perfil} )

