from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Categoria, Arquivo
from django.urls import reverse_lazy

# Create your views here.


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'materiais/formCategoria.html'
    success_url = reverse_lazy('inicio')


class ArquivoCreate(CreateView):
    model = Arquivo
    fields = ['idealizadora', 'descricao', 'categoria']
    template_name = 'materiais/formArquivo.html'
    success_url = reverse_lazy('inicio')

################# UPAGENS ###################


class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'materiais/formCategoria.html'
    success_url = reverse_lazy('inicio')


class ArquivoUpdate(UpdateView):
    model = Arquivo
    fields = ['idealizadora', 'descricao', 'categoria']
    template_name = 'materiais/formArquivo.html'
    success_url = reverse_lazy('inicio')


# class CategoriaList(ListView):
#     model = Categoria
#     template_name = 'paginas/listas/arqPriv.html'


# class ArquivoList(ListView):
#     model = Arquivo
#     template_name = 'paginas/listas/arquivo.html'
