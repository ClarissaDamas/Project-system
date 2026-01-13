#use the database

from django.db import models

class User(models.Model):

    Name = models.CharField(max_length=200, verbose_name='Nome completo') 
    cpf = models.CharField(max_length=11, blank=True, null=True, verbose_name='CPF')
    Telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='número de telefone')
    Email = models.EmailField(max_length=75, blank=True, null=True, verbose_name='Email') 
    DataNascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento') 

  

