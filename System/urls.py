from django.urls import path   
from . import views

#listar as funcoes na url

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Usuários', views.List_Usuario, name = 'caduser'),
]
