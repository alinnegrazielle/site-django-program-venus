from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Categoria, Arquivo
from django.urls import reverse_lazy

# Create your views here.


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'materiais/form-categoria.html'
    success_url = reverse_lazy('listar-categorias')


class ArquivoCreate(CreateView):
    model = Arquivo
    fields = ['idealizadora', 'descricao', 'categoria']
    template_name = 'materiais/form-arquivo.html'
    success_url = reverse_lazy('inicio')

##################### UPAGENS ######################


class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'materiais/form-categoria.html'
    success_url = reverse_lazy('listar-categorias')


class ArquivoUpdate(UpdateView):
    model = Arquivo
    fields = ['idealizadora', 'descricao', 'categoria']
    template_name = 'materiais/form-arquivo.html'
    success_url = reverse_lazy('inicio')

##################### UPAGENS ######################


class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'materiais/form-exc-cat.html'
    success_url = reverse_lazy('listar-categorias')


class ArquivoDelete(DeleteView):
    model = Arquivo
    template_name = 'materiais/form-exc-arq.html'
    success_url = reverse_lazy('inicio')

##################### LISTAGENS ######################


class CategoriaList(ListView):
    model = Categoria
    template_name = 'materiais/listas/categoria.html'


class ArquivoList(ListView):
    model = Arquivo
    template_name = 'materiais/listas/arquivo.html'
