from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Project, ProjectItem
from .form import addproject , ProjectItemForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'System/index.html') 

#Acessar lista de projetos existentes.
@login_required
def List_project(request):
    project = Project.objects.filter(dono=request.user).order_by('-id')
    #dicionario abaixo para receber os dados 
    return render(request, 'System/Projects.html', {'projects':project}) 

#Apresentar detalhes do projeto.
@login_required
def detalhes_project(request, project_id):
    dprojeto = get_object_or_404(Project, id = project_id)
    #dicionario abaixo para receber os dados 
    return render(request, 'System/detalhesprojeto.html', {'project':dprojeto} ) 

#Cadastrar novo projeto
@login_required
def add_project(request):
    if request.method != 'POST':
        form = addproject() #metodo GET mostra o forms vazio

    else:       
        form = addproject(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Projects'))

    return render(request, "System/addproject.html", {"form": form})

#Mostrar todos os subitens de um projeto.
@login_required
def Itens(request,project_id):
    project = Project.objects.get(id = project_id)
    itens = project.subitens.all().order_by('-id')
    return render(request, 'System/Itens.html', {'project':project, "itens": itens}) 


#Adicionar novo subitem do projeto
@login_required
def new_item(request, project_id):
    #acessar banco de dados de projetos
    project = get_object_or_404(Project, id=project_id)

    if request.method != 'POST':
        form = ProjectItemForm() 

    else:
        #acrescentar os dados antes de enviar
        form = ProjectItemForm(data=request.POST)

        if form.is_valid():
            #Nao salvar diretamente, acrescentar somente os dados
            new_item = form.save(commit=False)
            new_item.project = project
            new_item.save()
            #passar argumento do project ID 
            return HttpResponseRedirect(reverse('detalhesprojeto', args=[project_id]))

    return render(request, 'System/new_item.html', {'project':project, "form": form}) 

#Alterar um subitem existente.
@login_required
def edit_item(request, item_id):

    item = get_object_or_404(ProjectItem, id=item_id)
    project = item.project

    if request.method == 'POST':
        #Receber os dados do metodo post e substituir pelos dados que estavam na variavel ITEM
        form = ProjectItemForm(instance=item, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('Itens', project_id = project.id)
    else:
    
        form = ProjectItemForm(instance=item) #Apresenta o forms preenchido com os subitens registrados previamente.

#Tupla de project e Item para usar no html
    context = {
        'item': item, 
        'project': project, 
        'form': form    
    }

    return render(request, 'System/edit_item.html', context)

#Deletar um subitem existente
@login_required
def delete_item(request, item_id):

    item = get_object_or_404(ProjectItem, id=item_id)
    project = item.project


    if request.method != 'POST':
        form = ProjectItemForm(instance=item) 


    else:
        #Receber os dados e deletar 
        item.delete()
        return redirect('Itens', project_id = project.id)

    context = {
        'item': item, 
        'project': project, 
        'form': form    
    }

    return render(request, 'System/delete_item.html', context)




