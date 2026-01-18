from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # CPF e e-mail devem ser únicos (unique constraint)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(null=True, blank=True)
    #Não permitir salvar se “Aceite” não estiver marcado
    aceite_termos = models.BooleanField(default=False)

    def __str__(self):
        return self.username



