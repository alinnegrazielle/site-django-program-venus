from django.urls import path

# Importando views criadas
from .views import IndexView
from .views import CategoriaCreate, ArquivoCreate
from .views import CategoriaList, ArquivoList

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('criar/categoria', CategoriaCreate.as_view(), name='categoria'),
    path('upar/arquivo', ArquivoCreate.as_view(), name='upar_arquivo'),

    path('listar/categorias', CategoriaList.as_view(), name='listar_categorias'),
    path('listar/arquivos', ArquivoList.as_view(), name='listar_arquivos'),

]
