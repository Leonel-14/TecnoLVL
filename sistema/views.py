
from django.views.generic import TemplateView
# Create your views here.
class Inicio(TemplateView):
    template_name = 'html/index.html' #templates: ruta (html/pagina.html)
    
class Nosotros(TemplateView):
    template_name = 'html/nosotros.html'
    
class Ayuda(TemplateView):
    template_name = 'html/ayuda.html'
    