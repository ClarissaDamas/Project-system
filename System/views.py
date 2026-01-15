from django.shortcuts import render,get_object_or_404,redirect

from .models import Usuario
from .form import addperfil


def index(request):
    return render(request, 'System/index.html') 

def List_Usuario(request):
    #acessar banco de dados de usuarios
    user = Usuario.objects.all().order_by('-id')
    #dicionario abaixo para receber os dados 
    return render(request, 'System/Users.html', {'users':user}) 

def Perfil_Usuario(request, perfil_id):
    #apresentar o perfil
    perfil = get_object_or_404(Usuario, id = perfil_id)
    #dicionario abaixo para receber os dados 
    return render(request, 'System/perfil.html', {'perfil':perfil} ) 

def add_perfil(request):
    if request.method == 'POST':   #caso nao seja recebido post
        #Create a form instance from POST data.
        form = addperfil(request.POST)
        if form.is_valid(): 
            #Save a new addperfil object from the form's data.
            form.save() 
            #no deploy o dominio modifica, portanto nao pode colocar URL completa agora
            return redirect('Users')
    else:
        #se for GET mostra o forms vazio
        form = addperfil()
    return render(request, 'System/addperfil.html', {'form':form} )