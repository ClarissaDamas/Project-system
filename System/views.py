from django.shortcuts import render,get_object_or_404

from .models import Usuario


def index(request):
    return render(request, 'System/index.html') 

def List_Usuario(request):
    #acessar banco de dados de usuarios
    user = Usuario.objects.all()
    #dicionario abaixo para receber os dados 
    return render(request, 'System/Users.html', {'users':user}) 

def Perfil_Usuario(request, perfil_id):
    #apresentar o perfil
    perfil = get_object_or_404(Usuario, id = perfil_id)
    #dicionario abaixo para receber os dados 
    return render(request, 'System/perfil.html', {'perfil':perfil} ) 
