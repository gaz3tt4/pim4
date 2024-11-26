from django.shortcuts import render, redirect
from .utils import validar_login

def login(request):
    if request.method == "GET":
        username = request.GET.get('username')
        password = request.GET.get('password')
        if validar_login(request, username, password):
            return render(request, 'index.html')
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')
