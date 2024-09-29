from django.contrib import admin
from apps.orden.models import Orden
# Register your models here.
@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_venta','id_cliente','direccion_establecida','fecha_entrega')