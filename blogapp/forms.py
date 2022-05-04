"""Django's default forms for create new posts and promos"""

from django import forms

# App's models
from blogapp.models import Post, Promo


class NuevoPost(forms.ModelForm):
    """Form to add new posts."""
    
    class Meta:
        model = Post  # Modelo del cual importa
        fields = [
            'city',
            'title',
            'subtitle',
            'content',
            ]
        #  Widget para agrandar el area de texto(TextField) a 80 columnas
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}


class AgregarPromo(forms.ModelForm):
    """Form to add new promos."""
    class Meta:
        model = Promo
        fields = [
            'categoria',
            'descripcion',
            'detalle',
            'valid_through',
        ]
        # Widgets para agrandar el area de texto(CharField) a 80 columnas
        widgets = {
            'descripcion': forms.TextInput(attrs={'size': '80'}),
            'detalle': forms.TextInput(attrs={'size': '80'}),
            'valid_through': forms.SelectDateWidget(),
        }
