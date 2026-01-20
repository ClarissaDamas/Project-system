from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
#importar abaixo o model\classe Project
from .models import Project, ProjectItem 

#usar um modelo de usuário que estiver ativo neste projeto(usuários ativos podem ser gerenciados no admin do django)
User = get_user_model()

class AddCollaboratorForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['colaboradores']
    
    #Função de filtragem (__init__ cria uma subclass) --> no campo de colaboradores ao criar um novo subitem selecionar no formato checkbox e retornar somente usuários ativos no site

    def __init__(self, *args, **kwargs): #args recebe uma infinita lista,  e kwargs recebe infinitos elementos tornando um dicionário   
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






