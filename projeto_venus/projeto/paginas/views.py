from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Categoria, Arquivo
from django.urls import reverse_lazy

# Create your views here.


class IndexView(TemplateView):
    template_name = 'paginas/base.html'


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')


class ArquivoCreate(CreateView):
    model = Arquivo
    fields = ['idealizadora', 'descricao', 'arquivo', 'categoria']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')

################# UPAGENS ###################


class CategoriaList(ListView):
    model = Categoria
    template_name = 'paginas/listas/categoria.html'


class ArquivoList(ListView):
    model = Arquivo
    template_name = 'paginas/listas/arquivo.html'
