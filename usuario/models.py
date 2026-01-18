from django.db import models
from django.contrib.auth.models import AbstractUser,  BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone

class Usuario(AbstractUser):
    # email e username já são padrão, mas podemos forçar o email a ser único
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True) # 000.000.000-00 tem 14 caracteres
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(null=True, blank=True)
    aceite_termos = models.BooleanField(default=False)

    def __str__(self):
        return self.username



