from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
#Creo el formulario personalizado con la codicion de que es requerido llenar el campo
class RegistroUsuarioForm(UserCreationForm):
    nombre = forms.CharField(max_length=30,required=True)
    apellido = forms.CharField(max_length=30,required=True)
    email = forms.EmailField(max_length=100,required=True)
    
    class Meta:
        model = Usuario
        fields = ('nombre','apellido','username','password1','password2','email')

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Eliminar los textos de ayuda
            for field in self.fields.values():
                field.help_text = ""

class UsuarioUpdateForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30, required=True)
    apellido = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'username']