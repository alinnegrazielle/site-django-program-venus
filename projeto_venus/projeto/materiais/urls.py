from django.urls import path
from .views import CategoriaCreate, ArquivoCreate
from .views import CategoriaUpdate, ArquivoUpdate

urlpatterns = [
    path('criar/categoria', CategoriaCreate.as_view(), name='criar-categoria'),
    path('upar/arquivo', ArquivoCreate.as_view(), name='upar-arquivo'),

    path('editar/categoria/<int:pk>',
         CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/arquivo/<int:pk>', ArquivoUpdate.as_view(), name='editar-arquivo'),
]
