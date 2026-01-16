from django.urls import path   
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #criar novo caminho para login, diferente do padrao Django
    path('login', auth_views.LoginView.as_view(template_name='usuário/login.html'), name = 'login'),
    path('logout', views.logout_usuario, name = 'logout'),
    path('usuário/cadastrar.html', views.cadastrar, name = 'cadastrar'),
]