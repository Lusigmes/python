from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User # Autenticação/Validação de usuario no sistema

#renderizar o arquivo html na tela de cadastro
def cadastrar(request):
    # print(request.method)
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if not password == confirm_password:
            return redirect('/usuarios/cadastro/') # caso a senha digitada nao coincida, retorna a pagina inicial de cadastro
        
        user = User.objects.filter(username="luis") # filtra objetos da tabela
        print(user)
        
        # User.objects.create_user( # cadastro dusuario cadastrado no banco 
        #     username=username,
        #     password=password #criptografa hash de senha
        # )
        
        return HttpResponse("OK")    
    
    
    
    
    
    
    
    
    
    
# RECEBER OS DADOS DO FURMULARIO 
# NA VIEW PARA PROCESSR E SALVAR OS DADOS NO BANCO
# request.POST é o dicionario para pegar os dados