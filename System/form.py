from django import forms
from django.forms import ModelForm
#importar abaixo o model\classe Usuario
from .models import Usuario 

class addperfil(ModelForm):
    class Meta:
        model = Usuario
        fields = ["Name", "cpf", "Telefone", "Email","DataNascimento"]
        

