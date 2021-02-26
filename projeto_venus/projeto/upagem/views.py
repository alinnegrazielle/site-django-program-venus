from django.views.generic.edit import CreateView
from .models import Categoria, Arquivo
from django.urls import reverse_lazy

# Create your views here.
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'upagem/form.html'
    success_url = reverse_lazy('inicio')

class ArquivoCreate(CreateView):
    model = Arquivo
    fields = ['idealizadora', 'descricao', 'arquivo', 'categoria']
    template_name = 'upagem/form.html'
    success_url = reverse_lazy('inicio')