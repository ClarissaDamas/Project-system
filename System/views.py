from django.shortcuts import render 

from .models import Usuario


def index(request):
    return render(request, 'System/index.html') 

def List_Usuario(request):
    #acessar banco de dados de usuarios
    user = Usuario.objects.all()
    #dicionario abaixo para receber os dados ordenados
    #context = {'user':user}
    return render(request, 'System/caduser.html', {'users':user}) 
