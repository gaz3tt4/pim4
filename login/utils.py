from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import User

def validar_login(request, username, password):
    try:
        usuario = User.objects.get(username=username)
        if usuario.password == password:
            return True
        else:
            messages.error(request, "Senha incorreta.")
            return False
    except User.DoesNotExist:
        messages.error(request, "Usuário não encontrado.")
        return False