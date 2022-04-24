from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """Customization for new user registration form."""
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]