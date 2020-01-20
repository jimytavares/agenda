from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    
    class Meta:
        model = Contato
        fields = ('nome_contato', 'telefone_1', 'telefone_2', 'email')