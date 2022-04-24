from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from users.forms import RegisterForm

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
        'title': 'Registro usuario'
        }
    return render(request, 'registration/register.html', context)