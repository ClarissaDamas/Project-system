from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from .models import Project, ProjectItem 
from .form import addproject , ProjectItemForm , AddCollaboratorForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'System/index.html') 

def page_error(request):
    return render(request, 'System/error.html') 


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

    if dprojeto.dono == request.user: 
        return render(request, 'System/detalhesprojeto.html', {'project':dprojeto} )
    else:
        return render(request, 'System/error.html' )

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

    if project.dono  != request.user: 
        return render(request, 'System/error.html' )

    if request.method != 'POST':
        form = ProjectItemForm(project=project)

    else:
        #acrescentar os dados antes de enviar
        form = ProjectItemForm(data=request.POST, project = project)

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

    if project.dono  != request.user: 
        return render(request, 'System/error.html' )

    else:
       
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

@login_required
def manage_collaborators(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Segurança: Apenas o dono pode gerenciar colaboradores
    if request.user != project.dono:
        return HttpResponseForbidden("Apenas o dono pode adicionar colaboradores.")

    if request.method == 'POST':
        form = AddCollaboratorForm(request.POST, instance=project)
        if form.is_valid():
            form.save() # O ModelForm já lida com o ManyToMany automaticamente no save()
            return redirect('Itens', project_id=project.id)
    else:
        form = AddCollaboratorForm(instance=project)

    return render(request, 'System/manage_collaborators.html', {
        'project': project,
        'form': form
    })


