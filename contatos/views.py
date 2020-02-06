from django.shortcuts import render,redirect, get_object_or_404
#from django.http import HttpResponse
from .models import Contato, CadastrarAnime
from .forms import ContatoForm, AnimeForm, GastosForm

# Create your views here.

def contato_list(request):
    contatos = Contato.objects.all()
    return render(request, 'contato_list.html', {'contatos': contatos})
    
def contato_add(request):
    acao = "Adicionar Contato"
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contato_list')
    else:
        form = ContatoForm()        
    return render(request, 'contato_add.html',{'form': form})

def contato_edit(request, pk):
    acao = "Adicionar Contato"
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('contato_list')
    else:
        form = ContatoForm(instance=contato)        
    return render(request, 'contato_add.html',{'form': form, 'acao': acao})

def contato_del (request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    contato.delete()
    return redirect(contato_list)

def CadastrarAnime(request):
    title_cad_anime = "Cadastro de Animes"
    if request.method == "POST":
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CadastrarAnime')
    else:
        form = AnimeForm()        
    return render(request, 'cadastrar_anime.html',{'form': form})

def index(request):
    form = GastosForm()
    if request.method == "POST":
        form = GastosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CadastrarGastos')
    else:
        form = GastosForm()   
    return render(request, 'index.html',{'form': form})

def CadastrarGastos(request):
    title_cad_anime = "Cadastrar Gastos"
    if request.method == "POST":
        form = GastosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CadastrarGastos')
    else:
        form = GastosForm()        
    return render(request, 'cadastrar_gastos.html',{'form': form})