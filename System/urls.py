from django.urls import path   
from . import views

#listar as funcoes na url

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Users/', views.List_Usuario, name = 'Users'),
    path('perfil/<int:perfil_id>/', views.Perfil_Usuario, name = 'perfil'), #para acessar o perfil precisa registrar na barra http://127.0.0.1:8000/perfil/2/
]
