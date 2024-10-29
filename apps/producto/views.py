from django.views.generic import TemplateView, ListView
from apps.producto.models import Producto
from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.

class ProductoView(TemplateView):
    template_name = "html/productos.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productosX"] = Producto.objects.all()
        return context
    
