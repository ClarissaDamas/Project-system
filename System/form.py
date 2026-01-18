from django import forms
from django.forms import ModelForm
#importar abaixo o model\classe Project
from .models import Project, ProjectItem 



class addproject(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "objetivo", "datainicio", "datafinal", "dono", "colaboradores"]
        #campo widgets adicionado com IA
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'objective': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Máximo 250 caracteres'}),
        }
        
class ProjectItemForm(forms.ModelForm):
    class Meta:
        model = ProjectItem
        fields = '__all__'
    #campo widgets adicionado com IA
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }


