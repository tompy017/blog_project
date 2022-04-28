"""Forms for users app. Register new user; update profiles; messages."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# My models
from users.models import Avatar, Message


# Forms


class RegisterForm(UserCreationForm):
    """Customization for new user registration form."""
    
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Reingrese contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class UpdateProfileForm(UserCreationForm):
    """Customization for new user registration form."""
    
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)    
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Reingrese contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]


class AvatarForm(forms.ModelForm):
    """Avatar form"""

    class Meta:
        model = Avatar
        fields = ['avatar',]


class MessageForm(forms.ModelForm):
    """DM's form"""
    
    class Meta:
        model = Message  # Modelo del cual importa
        fields = [
            'receiver',
            'msg',
        ]
        #  Widget para agrandar el area de texto(TextField) a 80 columnas
        widgets = {'msg': forms.Textarea(attrs={'cols': 80})}
