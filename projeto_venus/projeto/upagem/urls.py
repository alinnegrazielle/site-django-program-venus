from django.urls import path
from .views import CategoriaCreate, ArquivoCreate

urlpatterns = [
    path('criar/categoria', CategoriaCreate.as_view(), name='categoria'),
    path('upar/arquivo', ArquivoCreate.as_view(), name='upar_arquivo'),
]