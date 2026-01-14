from django.shortcuts import render 

from .models import Usuario


def index(request):
    return render(request, 'System/index.html') 

def Usuario(request):
    #acessar banco de dados de usuarios
    #user = user.objects.order_by('data_added')
    #dicionario abaixo para receber os dados ordenados
    #context = {'user':user}
    return render(request, 'System/caduser.html') 
