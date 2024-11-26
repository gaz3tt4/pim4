from .models import User
from django.contrib import messages

def validar_login(request, username, password):
    try:
        usuario = User.objects.get(username=username)
        if usuario.password == password:
            messages.success(request, "Usuário autenticado.")
            return True
        else:
            messages.error(request, "Senha incorreta.")
            return False
    except User.DoesNotExist:
        messages.error(request, "Usuário inexistente.")
        return False
