from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from datetime import date


class cadastrarform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        #Utilizar campos do usercreation e adicionar campos do model criado.
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email", "cpf", "telefone", "data_nascimento", "aceite_cadastro", )
        #Widgets no campo cpf e telefone 
        widgets = { 'cpf': forms.TextInput(attrs={'class': 'cpf', 'placeholder': '000.000.000-00'}), 'telefone' : forms.TextInput(attrs={'class': 'telefone', 'placeholder': '(00) 00000-0000'}), 'data_nascimento':  forms.DateInput(attrs={'type': 'date'}) }
                   
    def get_full_name(self):
        #Nome completo
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    # Validar dados(cpf,nascimento e aceite) com a função clean_cpf antes de salvar no banco de dados.
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf)!= 14:
            raise forms.ValidationError("O CPF deve ter 11 dígitos.")
        return cpf

    # Validar Data de Nascimento
    def clean_data_nascimento(self):
        data = self.cleaned_data.get('data_nascimento')
    #A data de nascimento não pode ser no futuro    
        if data and data > date.today():
            raise forms.ValidationError("Insira uma data de nascimento válida")
        return data

    #Validar Aceite
    def clean_aceite_cadastro(self):
        aceite = self.cleaned_data.get('aceite_cadastro')
        if not aceite:
            raise forms.ValidationError("Você precisa aceitar para continuar.")
        return aceite