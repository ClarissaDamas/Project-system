from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from .models import Project, ProjectItem 
from .form import addproject , ProjectItemForm , AddCollaboratorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


def index(request):
    return render(request, 'System/index.html') 

def page_error(request):
    return render(request, 'System/error.html') 


#Acessar lista de projetos existentes(permitido dono ou colaborador)
@login_required
def List_project(request):
    project_dono = Project.objects.filter(dono=request.user)
    project_colaborador = Project.objects.filter(colaboradores=request.user)
    project = (project_dono | project_colaborador).distinct().order_by('-id')
    return render(request, 'System/Projects.html', {'projects':project}) 

#Apresentar detalhes do projeto(permitido dono ou colaborador)
@login_required
def detalhes_project(request, project_id):
    dprojeto = get_object_or_404(Project, id = project_id)

    # Verifica se o usuário logado é o dono OU colaborador
    if request.user == dprojeto.dono or request.user in dprojeto.colaboradores.all():
        return render(request, 'System/detalhesprojeto.html', {'project':dprojeto} )
    else:
        return render(request, 'System/error.html' )



#Cadastrar novo projeto(permitido todos logados)
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

# Mostrar subitens de um projeto (dono tem acesso a todos os subitens; colaborador tem acesso apenas aos subitens pelos quais é responsável)
@login_required
def Itens(request, project_id):
    project = Project.objects.get(id = project_id)
    responsavel_objetos = ProjectItem.objects.filter(project=project, resp=request.user)
    if project.dono  == request.user: 
        itens = project.subitens.all().order_by('-id') 
    elif responsavel_objetos.exists():
        itens = project.subitens.filter(resp=request.user).order_by('-id')
    else:
        return render(request, 'System/error.html' )
    return render(request, 'System/Itens.html', {'project':project, "itens": itens}) 


#Adicionar novo subitem do projeto (permitido dono )
@login_required
def new_item(request, project_id):
    #acessar banco de dados de projetos
    project = get_object_or_404(Project, id=project_id)

    if request.method != 'POST':
        form = ProjectItemForm()
          
    if project.dono  == request.user: #Para mudar e os colaboradores\Responsável conseguirem criar um novo SUBITEM basta adicionar depois de request.user --> or request.user in project.colaboradores.all()   
                
        form = ProjectItemForm(data=request.POST) #acrescentar os dados antes de enviar
        project_dono = get_user_model().objects.filter(id=project.dono.id)
        project_colaborador = project.colaboradores.all()
        form.fields['resp'].queryset = (project_dono | project_colaborador).distinct().order_by('-id')   #No campo responsável do forms, adicionar somente se for o dono ou colaborador do projeto. Se alterar para todos os usuários, remover o filtro, se alterar para mais de um colaborador trocar em MODELS.py para Many_to_Many e filtrar usando __init__ em FORM.py
        if form.is_valid():
            new_item = form.save(commit=False)  #Nao salvar diretamente, acrescentar somente os dados
            new_item.project = project
            new_item.save()
            return HttpResponseRedirect(reverse('detalhesprojeto', args=[project_id]))  #passar argumento do project ID 
        

    else:
        return render(request, 'System/error.html' )


    return render(request, 'System/new_item.html', {'project':project, "form": form}) 


#Alterar um subitem existente. (dono e colaborador responsável)
@login_required
def edit_item(request, item_id):
    item = get_object_or_404(ProjectItem, id=item_id)
    project = item.project

    if project.dono  != request.user or request.user in project.colaboradores.all():
        return render(request, 'System/error.html' )

    else:
       
        if request.method == 'POST':
            # Receber os dados do método POST e substituir pelos dados que estavam na variável ITEM
            form = ProjectItemForm(instance=item, data= request.POST)
            if form.is_valid():
                form.save()
                return redirect('Itens', project_id = project.id)
        else:
    
                form = ProjectItemForm(instance=item)#Apresenta o forms preenchido com os subitens registrados previamente.


    return render(request, 'System/edit_item.html', {'item':item, 'project': project, 'form': form})


#Deletar um subitem existente (permitido dono-button não aparece para colaborador responsável)
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


    return render(request, 'System/delete_item.html', {'item':item, 'project': project, 'form': form})

#Gerenciar usuários com acesso ao projeto(permitido dono)
@login_required
def manage_collaborators(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if project.dono  != request.user or request.user in project.colaboradores.all():
        return HttpResponseForbidden("Apenas o dono pode adicionar colaboradores.")

    if request.method == 'POST':
        form = AddCollaboratorForm(request.POST, instance=project)
        if form.is_valid():
            form.save() # O ModelForm já lida com o ManyToMany automaticamente no save()
            return redirect('Itens', project_id=project.id)
    else:
        form = AddCollaboratorForm(instance=project)

    return render(request, 'System/manage_collaborators.html', {'project':project, 'form': form})


