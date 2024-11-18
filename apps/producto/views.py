from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Producto
from apps.comentario.models import Comentario
from apps.usuario.models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.comentario.forms import ComentarioForm
# Create your views here.

class ProductoView(TemplateView):
    template_name = 'html/productos.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Esto verifica si el usuario genero una solicitud de tipo get
        ordenar_por_precio = self.request.GET.get('ordenar', 'asc')

        if ordenar_por_precio == 'asc':
            productos = Producto.objects.all().order_by('precio')  # Orden ascendente
        else:
            productos = Producto.objects.all().order_by('-precio')  # Orden descendente

        context["productos"] = productos
        return context


class ProductoDetallesView(LoginRequiredMixin,TemplateView):
    template_name = 'html/producto_detalles.html'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Agrega los datos adicionales que necesitas
        producto = get_object_or_404(Producto, id=kwargs['pk'])
        comentarios = Comentario.objects.filter(producto=kwargs['pk'])
        form = ComentarioForm()
        
        context['producto'] = producto
        context['comentarios'] = comentarios
        context['form'] = form
        
        return context

    def post(self, request, *args, **kwargs):
        producto = get_object_or_404(Producto, id=kwargs['pk'])
        form = ComentarioForm(request.POST)
        
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.producto = producto
            comentario.save()
            return redirect('producto_detalles', pk=producto.id)
        
        else:
            return redirect('producto_detalles', pk=producto.id)
        
    
    


