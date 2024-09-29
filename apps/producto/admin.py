from django.contrib import admin
from apps.producto.models import Categoria, EstadoProducto, Producto
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(EstadoProducto)
class EstadoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'id_estado_producto', 'nombre', 'marca', 'precio', 'stock', 'imagen', 'descripcion')