from django import forms 
from .models import Cliente

class ClientForm(forms.ModelForm):  
    class Meta:
        model = Cliente
        fields = ['cli_st_nome', 'cli_st_doc', 'cli_st_endereco', 'cli_st_cidade', 'cli_st_estado', 'cli_st_telefone', 'cli_st_email']  
        labels = {
            'cli_st_nome': 'Nome',
            'cli_st_doc': 'Doc',
            'cli_st_endereco': 'Endereço',
            'cli_st_cidade': 'Cidade',
            'cli_st_lei': 'Lei',
            'cli_st_telefone': 'Telefone',
            'cli_st_email': 'Email',
        }
        