from django import forms
from .models import Contato, CadastrarAnime, CadastrarGastos


class ContatoForm(forms.ModelForm):
    
    class Meta:
        model = Contato
        fields = ('nome_contato', 'telefone_1', 'telefone_2', 'email')
        
        
class AnimeForm(forms.ModelForm):
    
    class Meta: 
        model = CadastrarAnime
        fields = ('nome_anime', 'temporada')
        
        
class GastosForm(forms.ModelForm):
    
    class Meta:
        model = CadastrarGastos
        fields = ('nome_produto', 'valor', 'parcela', 'comentario')