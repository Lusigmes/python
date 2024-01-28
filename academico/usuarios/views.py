from django.shortcuts import render
from django.http import HttpResponse

#renderizar o arquivo html na tela de cadastro
def cadastrar(request):
    # print("Request[", request,"]")
    return render(request, 'cadastro.html')