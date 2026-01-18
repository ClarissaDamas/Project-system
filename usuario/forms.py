from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from datetime import date
import re


class cadastrarform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ("email", "cpf", "telefone", "data_nascimento", "aceite_termos")

    # Validar CPF (Lógica simplificada de dígitos)
    def clean_cpf(self):
        cpf = re.sub(r'\D', '', self.cleaned_data.get('cpf')) # Remove pontos e traços
        if len(cpf) != 11:
            raise forms.ValidationError("O CPF deve ter 11 dígitos.")
        # Aqui você pode inserir uma lógica completa de cálculo de dígitos verificadores
        return self.cleaned_data.get('cpf')

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