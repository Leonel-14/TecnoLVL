from django.contrib import admin
from apps.ubicacion.models import Barrio, Ciudad, Provincia, Pais

# Register your models here.
@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre','id_ciudad')
@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre','id_provincia')

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre','id_pais')

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)