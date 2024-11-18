from django.urls import path,include
from .views import RegistroUsuario,Perfil,exit

urlpatterns = [path('accounts/', include('django.contrib.auth.urls')),
               path('registro/',RegistroUsuario.as_view(),name='registro'),
               path('perfil/',Perfil.as_view(),name='perfil'),
                path('exit/',exit,name='exit')
               ]