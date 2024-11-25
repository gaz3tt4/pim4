from django.shortcuts import render, redirect
from .utils import validar_login

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if validar_login(request, username, password):
            return redirect('index')  # Redireciona para a página inicial
        else:
            return redirect('loginTemplate')  # Retorna para a página de login

    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')