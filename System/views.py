from django.shortcuts import render

from django.shortcuts import render # Importa a função render

def index(request):
    #contexto = {'nome': 'Django', 'versao': 4}
    return render(request, 'System/index.html') 


