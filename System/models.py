#use the database
from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome projeto') 
    #Um projeto sempre pertence a um usuário (dono)
    dono  = models.ForeignKey( settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='owned_projects',  verbose_name='Dono do Projeto')
    #Um projeto pode ter vários colaboradores e um usuário pode estar em vários projetos
    colaboradores = models.ManyToManyField( settings.AUTH_USER_MODEL, default="Sem colaboradores", related_name='collaborating_projects', verbose_name='Colaboradores'
    )
    objetivo = models.TextField(default= "Insira objetivo",max_length=250 , verbose_name='Descrição curta em 250 caracteres')
    datainicio = models.DateField(default="AAAA-MM-DD",verbose_name='Data inicial')
    datafinal = models.DateField(default="AAAA-MM-DD", verbose_name='Data final') 

    class Meta:
         verbose_name= 'Projeto'
         verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.name
    
class ProjectItem(models.Model):
    TYPE_CHOICES = (
        ('T', 'Tarefas'),
        ('E', 'Entregas'),
        ('A', 'Etapas'),
        ('M', 'Melhorar'),
        ('R', 'Revisar'),
        ('O', 'Outro'),
    )
    STATUS_CHOICES = (
        ('P', 'Pendente'),
        ('A', 'Em andamento'),
        ('C', 'Concluído'),
    )
    #O project do modelo PROJETO esta ligado ao project do modelo PROJECTITEM por uma chave estrangeira 
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subitens', verbose_name='Projeto')
    resp = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.PROTECT, related_name='Responsavel',  verbose_name='Responsável pelo subitem')
    title = models.CharField(max_length=200, verbose_name='Título')
    description =  models.TextField( verbose_name='Descrição')
    #blank e null True para ser opcional
    prazo = models.DateField(blank=True, null=True, verbose_name='Data final prevista(opcional)')
    status  = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Status')
    tipo  = models.CharField(default='O', max_length=1, choices=TYPE_CHOICES, verbose_name='Tipo')

    class Meta:
        verbose_name='Subitem do projeto'
        verbose_name_plural ='Subitens dos projetos'

    def __str__(self):
    #aparecer somente os primeiros 50 caracteres
        return f"{self.title} - Responsável: {self.resp.username}"
    

