from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Usuario
from .form import addperfil
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'System/index.html') 

@login_required
def List_Usuario(request):
    #acessar banco de dados de usuarios
    user = Usuario.objects.all().order_by('-id')
    #dicionario abaixo para receber os dados 
    return render(request, 'System/Users.html', {'users':user}) 

@login_required
def Perfil_Usuario(request, perfil_id):
    #apresentar o perfil
    perfil = get_object_or_404(Usuario, id = perfil_id)
    #dicionario abaixo para receber os dados 
    return render(request, 'System/perfil.html', {'perfil':perfil} ) 

@login_required
def add_perfil(request):
    if request.method != 'POST':

        form = addperfil() #metodo GET mostra o forms vazio

    else:
        
        form = addperfil(request.POST)

        if form.is_valid():
            #Save a new addperfil object from the form's data.
            form.save()
             #no deploy o dominio modifica, portanto nao pode colocar URL completa agora
            return HttpResponseRedirect(reverse('Users'))

    return render(request, "System/addperfil.html", {"form": form})



