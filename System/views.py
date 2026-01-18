from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Project, ProjectItem
from .form import addproject , ProjectItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView



def index(request):
    return render(request, 'System/index.html') 

@login_required
def List_project(request):
    #acessar banco de dados de usuarios
    project = Project.objects.all().order_by('-id')
    #dicionario abaixo para receber os dados 
    return render(request, 'System/Projects.html', {'projects':project}) 

@login_required
def detalhes_project(request, project_id):
    #apresentar o perfil
    dprojeto = get_object_or_404(Project, id = project_id)
    #dicionario abaixo para receber os dados 
    return render(request, 'System/detalhesprojeto.html', {'project':dprojeto} ) 

@login_required
#Cadastro de Projeto
def add_project(request):
    if request.method != 'POST':

        form = addproject() #metodo GET mostra o forms vazio

    else:
        
        form = addproject(request.POST)

        if form.is_valid():
            #Save a new project
            form.save()
             #no deploy o dominio modifica, portanto nao pode colocar URL completa agora
            return HttpResponseRedirect(reverse('Projects'))

    return render(request, "System/addproject.html", {"form": form})

@login_required
def Itens(request,project_id):
    #mostra todos os itens de um projeto
    project = Project.objects.get(id = project_id)
    itens = project.subitens.all().order_by('-id')
    return render(request, 'System/Itens.html', {'project':project, "itens": itens}) 


@login_required
#Adicionar novo subitem do projeto
def new_item(request, project_id):
    #acessar banco de dados de projetos
    project = get_object_or_404(Project, id=project_id)

    if request.method != 'POST':
        form = ProjectItemForm() #metodo GET mostra o forms vazio

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


@login_required
def edit_item(request, item_id):
    #Altera um subitem criado.
    item = get_object_or_404(ProjectItem, id=item_id)
    project = item.project


    if request.method == 'POST':
        #Receber os dados do metodo post e substituir pelos dados que estavam na variavel ITEM
        form = ProjectItemForm(instance=item, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('Itens', project_id = project.id)
    else:
        # formulário com erros 
        form = ProjectItemForm(instance=item) #Apresenta o forms preenchido com os subitens registrados previamente.

    context = {
        'item': item, 
        'project': project, 
        'form': form    
    }



#Tupla de project e Item para usar no html e fazer possiveis alteracoes
    return render(request, 'System/edit_item.html', context)


