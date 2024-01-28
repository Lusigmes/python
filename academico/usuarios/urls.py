from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar, name="cadastro"), #criando rota para cadastro de uruarios /usuarios/cadastro
    
]
