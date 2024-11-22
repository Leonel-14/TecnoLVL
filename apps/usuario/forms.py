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

    def clean(self):
        datos = super().clean()
        password1 = datos.get('password1')
        password2 = datos.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return datos

class UsuarioUpdateForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30, required=True)
    apellido = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'username']