from django.contrib import admin
from django.contrib.auth import decorators
from .models import Usuario
# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','username']
    search_fields = ['nombre',]
    list_filter = ['username',]
    