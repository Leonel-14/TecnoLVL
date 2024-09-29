from django.contrib import admin
from apps.venta.models import EstadoVenta, Venta, DetalleVenta
# Register your models here.
@admin.register(EstadoVenta)
class EstadoVentaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_estado_venta','fecha_venta','total_venta')


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'id_venta', )