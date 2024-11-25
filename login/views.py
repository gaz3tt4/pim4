from django.shortcuts import render, redirect
from .utils import validar_login

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

    return render(request, 'login.html')


