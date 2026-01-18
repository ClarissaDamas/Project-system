from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from datetime import date


class cadastrarform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        #Utilizar campos do usercreation e adicionar campos do model criado.
        fields = UserCreationForm.Meta.fields + ("email", "cpf", "telefone", "data_nascimento", "aceite_termos")
        #widgets no campo cpf e telefone 
        widgets = { 'cpf': forms.TextInput(attrs={'class': 'cpf', 'placeholder': '000.000.000-00'}), 'telefone' : forms.TextInput(attrs={'class': 'telefone', 'placeholder': '(00) 00000-0000'}), }

    # Validar CPF (Lógica simplificada de dígitos)
    def clean_cpf(self):
    #Se o tamanho do self.cpf for maior que 11 retorna erro(cpf válido)
        cpf = self.cleaned_data.get('cpf')
        if len(cpf)!= 11:
            raise forms.ValidationError("O CPF deve ter 11 dígitos.")
        return cpf

    # Validar Data de Nascimento
    def clean_data_nascimento(self):
        data = self.cleaned_data.get('data_nascimento')
        if data and data > date.today():
            raise forms.ValidationError("A data de nascimento não pode ser no futuro.")
        return data

    # Validar Aceite
    def clean_aceite_termos(self):
        aceite = self.cleaned_data.get('aceite_termos')
        if not aceite:
            raise forms.ValidationError("Você precisa aceitar os termos para continuar.")
        return aceite