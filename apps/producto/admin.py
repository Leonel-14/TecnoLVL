from django.contrib import admin
from .models import Producto, Tipo
# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','tipo','imagen','marca','descripcion']
    
@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    lista_display = ['nombre',]