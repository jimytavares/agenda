from django.db import models

    # Create your models here.

class Contato(models.Model):
    nome_contato = models.CharField(max_length=100, verbose_name='Nome Completo')
    telefone_1   = models.CharField(max_length=11, verbose_name='Telefone Principal')
    telefone_2   = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone Secundario')
    email        = models.EmailField(verbose_name='Email')

    def __str__ (self):
        return self.nome_contato
    
    
class CadastrarAnime(models.Model):
    nome_anime = models.CharField(max_length=50, verbose_name='Nome Anime')
    temporada = models.CharField(max_length=50, verbose_name='Temporada')
    
    def __str__ (self):
        return self.nome_anime
    