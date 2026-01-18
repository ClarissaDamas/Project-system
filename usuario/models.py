from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # CPF e e-mail devem ser únicos (unique constraint)
    username = models.CharField(max_length=50, unique=True, verbose_name='Usuário')
    first_name = models.CharField(max_length=200, verbose_name='Nome') 
    last_name = models.CharField(max_length=200, verbose_name='Sobrenome') 
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    #Não permitir salvar se “Aceite” não estiver marcado
    aceite_cadastro  = models.BooleanField(default=False)

    class Meta:
        verbose_name= 'Usuário'
        verbose_name_plural = 'Usuários'


    def __str__(self):
        return self.username


