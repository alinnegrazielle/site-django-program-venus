from django.urls import path
from .views import IndexView, DiretoriaView, AcPrivView, AcPubView

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('acervoprivado', AcPrivView.as_view(), name='acpriv'),
    path('acervopublico', AcPubView.as_view(), name='acpub'),
]
