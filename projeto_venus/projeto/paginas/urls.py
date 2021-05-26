from django.urls import path

# Importando views criadas
from .views import IndexView
# from .views import CategoriaList, ArquivoList

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),

    # path('listar/arquivos/priv', CategoriaList.as_view(),
    #      name='listar_arquivos_priv'),
    # path('listar/arquivos', ArquivoList.as_view(), name='listar_arquivos'),

]
