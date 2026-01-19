from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
#importar abaixo o model\classe Project
from django.db.models import Q
from .models import Project, ProjectItem 
from django.db import models

#usar um modelo de usuário que estiver ativo neste projeto(usuários ativos podem ser gerenciados no admin do django)
User = get_user_model()

class AddCollaboratorForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['colaboradores']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['colaboradores'].widget = forms.CheckboxSelectMultiple()
        self.fields['colaboradores'].queryset = get_user_model().objects.all()


  
class addproject(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "objetivo", "datainicio", "datafinal", "dono", "colaboradores"]
        #campo widgets adicionado com IA
        widgets = {
            'datainicio': forms.DateInput(attrs={'type': 'date'}),
            'datafinal': forms.DateInput(attrs={'type': 'date'}),
            'objetivo': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Máximo 250 caracteres'}),}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['colaboradores'].widget = forms.CheckboxSelectMultiple()
        self.fields['colaboradores'].queryset = get_user_model().objects.all()

        
class ProjectItemForm(forms.ModelForm):
    class Meta:
        model = ProjectItem
        fields = ["resp", "title", "description", "prazo", "status", "tipo"]

    #campo widgets adicionado com IA
        widgets = {
            'prazo': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    #Funcao de filtrar adicionada com IA
    def __init__(self, *args, **kwargs):
        # Recebemos o projeto via view para filtrar os usuários
        project = kwargs.pop('project', None)
        super().__init__(*args, **kwargs)
        
        if project:
            # Filtra para mostrar apenas o dono OU colaboradores do projeto
            self.fields['resp'].queryset = User.objects.filter( models.Q(id=project.dono.id) | models.Q(collaborating_projects=project) ).distinct()






