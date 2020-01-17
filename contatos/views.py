from django.shortcuts import render
#from django.http import HttpResponse
from .models import Contato

# Create your views here.

def contato_list(request):
    contatos = Contato.objects.all()
    return render(request, 'contato_list.html', {'contatos': contatos})
    