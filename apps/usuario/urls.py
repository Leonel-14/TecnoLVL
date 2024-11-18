from django.urls import path,include
from .views import RegistroUsuario,Perfil,exit,Logueo

urlpatterns = [
            path("login/", Logueo.as_view(), name="login"),
            path('registro/',RegistroUsuario.as_view(),name='registro'),
            path('perfil/',Perfil.as_view(),name='perfil'),
            path('exit/',exit,name='exit')
               
]