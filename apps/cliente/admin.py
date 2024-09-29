from django.contrib import admin
from apps.cliente.models import Cliente
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','dni','edad','correo','contraseña','telefono','id_barrio','calle','altura','piso','departamento','codigo_postal')
