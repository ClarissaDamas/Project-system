from django.urls import path   
from . import views

#listar as funcoes na url

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Projects/', views.List_project, name = 'Projects'),
    path('detalhesprojeto/<int:project_id>/', views.detalhes_project, name = 'detalhesprojeto'), #para acessar o perfil precisa registrar na barra http://127.0.0.1:8000/perfil/2/
    path('addproject', views.add_project, name = 'addproject'),
    path('new_item/<int:project_id>' , views.new_item, name = 'new_item'),
    path('Itens/<int:project_id>/', views.Itens, name = 'Itens'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    #path('delete_item/<int:item_id>', views.delete_item, name = 'delete_item'),
]
