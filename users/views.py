from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from django.views.generic.detail import DetailView

from users.forms import RegisterForm, UpdateProfileForm
from users.models import Avatar

# Create your views here.

def register(request):
    """Register a new user."""

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        # form = UserCreationForm() replaced by customized RegisterForm (from users/forms.py)
        form = RegisterForm()

    else:
        # Paso formulario con datos ingresados por POST
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Para loguearse al crear nuevo usuario uso funcion login() de django.contrib.auth
            login(request, new_user)
            # Redirecciono a Inicio con usuario ya logueado
            return redirect('blogapp:Inicio')

    context = {
        'form': form,
        'title': 'Registro usuario',
        'warnings': [
            'El nombre de usuario no puede ser mayor a 150 caracteres. Solo letras, numeros y "@/./+/-/_"',
            'La contraseña no puede ser similar a tus datos registrados',
            'La contraseña debe contener al menos 8 caracteres y debe contener aunque sea una letra y un numero',
        ]
    }
    return render(request, 'registration/register.html', context)

@login_required
def update_profile(request):
    """Update user profile."""
    
    user = request.user
    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = UpdateProfileForm(instance=user)

    else:
        # Data submitted. Formulario para guardar con los datos enviados por POST
        form = UpdateProfileForm(instance=user, data=request.POST)
        if form.is_valid():
            edited_user = form.save()
            # Login if user requested a password or username change (if not, user  would be logged out)
            login(request, edited_user)
            return redirect('blogapp:Inicio')
    context = {
        'title': 'Actualizar',
        'subtitle': 'Actualizar usuario',
        'form': form,
        'avatar': avatar
    }
    return render(request, 'registration/update_profile.html', context)


# CBV

# class Profile(LoginRequiredMixin, DetailView):
#     model = User
#     template_name = 'users/profile.html'
@login_required
def profile(request, user_id):
    user = request.user

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    context = {
        'user': user,
        'avatar': avatar,
        'title': 'Profile',
    }
    return render(request, 'users/profile.html', context)

