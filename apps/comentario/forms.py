from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    descripcion = forms.CharField(
        label="",
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Deja tu comentario aquí',
                'id': 'floatingTextarea',
                'style': 'height: 150px',
            }
        )
    )

    class Meta:
        model = Comentario
        fields = ['descripcion',]
        
        
    