from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/base.html'

class DiretoriaView(TemplateView):
    template_name = 'paginas/diretoria.html'

class AcPrivView(TemplateView):
    template_name = 'paginas/acpriv.html'

class AcPubView(TemplateView):
    template_name = 'paginas/acpub.html'