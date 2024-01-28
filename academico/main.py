#django-admin startproject estudo_academico . # criar django project
#python manage.py startapp usuarios . # criar app
#.venv\Scripts\activate -> cd estudo_academico? -> python manage.py runserver
# python manage.py migrate # criar bancos


# 1:32:00


# mvt model-view-template
# model = camada de conexao com bd
# view = processa os dados
# template = interface da aplicação 


# criar rotas -> importar templates(config static) -> db (model?) migrate ->

#[1] autenticação para login do usuario
#[2]
#[3]
#[4]
#[5]

# inserir linha abaixo no form, para receber dados do formulario 
# <form method="post" action="{% url 'cadastro' %}">      {% csrf_token %}
# cadastro referente ao name = "cadastro" em /usuarios/urls.py


"""
    após uma requisição do usuário 
    irá para o roteamento de urls
    após o urls irá acessar as views (árquivos de processamento )
    
"""