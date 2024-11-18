from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Comentario
        fields = ['descripcion',]
        
        
    