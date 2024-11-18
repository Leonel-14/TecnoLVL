from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Inicio(TemplateView):
    template_name = 'html/index.html' #templates: ruta (html/pagina.html)
    
    def mostrar_inicio(request):
        return render(request,'index')

class Nosotros(TemplateView):
    template_name = 'html/nosotros.html'
    
    def mostrar_acerca(request):
        return render(request,'nosotros')
    
class Ayuda(TemplateView):
    template_name = 'html/ayuda.html'
    
    def mostrar_ayuda(request):
        return render(request,'ayuda.html')