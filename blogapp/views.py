"""Views for blog; home, posts and promos"""

from django.shortcuts import render, redirect
# CBV
from django.views.generic.edit import DeleteView
# Decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# My models and forms
from blogapp.models import Post, Promo
from blogapp.forms import NuevoPost, AgregarPromo
from users.models import Avatar



# Create your views here.

def inicio(request):
    """Home page for blogapp."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    context = {
        'avatar': avatar,
        'title': 'Inicio',
        'message': 'Bienvenidos a City Travel',
        'subtitle': '¿Planificando tu próximo viaje? '
                'Lee las recomendaciones realizadas por los propios miembros del blog!',
        }
    return render(request, 'blogapp/index.html', context)


def promos(request):
    """View for promotions page."""
    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''
    
    # Defino variable conteniendo todas las promociones  
    promos = Promo.objects.order_by('-valid_through')
    
    # Buscar promos por categoria
    category = request.GET.get('categoria')

    if category:
        promos = Promo.objects.filter(categoria__icontains=category)
        context = {
            'title': 'Promos',
            'category': category,
            'search': 'Buscar por categoría (ej: "Alojamiento")',
            'promos': promos,
            'avatar': avatar,
        }
        return render(request, 'blogapp/promos.html', context)

    else:
        # Listar todas las promociones
        context = {
            'promos': promos,
            'title': 'Promos',
            'subtitle': '¡Mira las promociones que hay para tu viaje!',
            'search': 'Buscar por categoría (ej: "Alojamiento")',
            'avatar': avatar,
        }
        return render(request, 'blogapp/promos.html', context)


def posts(request):
    """View for posts page."""
    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    # Defino variable conteniendo todos los posts ordenados de mas nuevo a mas antiguo
    posts = Post.objects.order_by('-date_added')

    # Para buscar posts por ciudad
    city = request.GET.get('city')
    if city:
        posts = Post.objects.filter(city__icontains=city)
        context = {
            'title': 'Posts',
            'city': city,
            'search': 'Buscar por ciudad',
            'posts': posts,
            'avatar': avatar,
        }
        return render(request, 'blogapp/posts.html', context)
    
    else:
        # Listar todos los posts
        context = {
            'posts': posts,
            'title': 'Posts',
            'subtitle': '¡El listado completo de nuestros posts!',
            'search': 'Buscar por ciudad',
            'avatar': avatar,
        }
        return render(request, 'blogapp/posts.html', context)


@login_required
def agregar_promos(request):
    """View to add new promotions."""
    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = AgregarPromo()

    else:
        # Data submitted. Paso formulario con datos ingresados por POST
        form = AgregarPromo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogapp:Promos')

    context = {
        'form': form,
        'title': 'Agregar Promo',
        'avatar': avatar,
    }
    return render(request, 'blogapp/new_promo.html', context)


@login_required
def agregar_post(request):
    """View to add new posts."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = NuevoPost()
    
    else:
        # Data submitted. Paso formulario con datos ingresados por POST
        form = NuevoPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogapp:Posts')

    context = {
        'form': form, 
        'title': 'Nuevo Post',
        'avatar': avatar,
    }
    return render(request, 'blogapp/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit an existing post."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    # Post que se va a editar
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # No data submitted. Formulario ya poblado con los datos a editar (antes de enviar/guardar)
        form = NuevoPost(instance=post)

    else:
        # Data submitted. Formulario para guardar con los datos enviados por POST
        form = NuevoPost(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogapp:Posts')

    context = {
        'title': 'Edit',
        'subtitle': post.title,
        'form': form,
        'avatar': avatar,
    }
    return render(request, 'blogapp/edit_post.html', context)
    

@login_required
def edit_promo(request, promo_id):
    """Edit an existing promo."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    # Promocion a editar
    promo = Promo.objects.get(id=promo_id)

    if request.method != 'POST':
        # No data submitted. Formulario ya poblado con datos a editar (antes de enviar/guardar)
        form = AgregarPromo(instance=promo)
    
    else:
        # Data submitted. Formulario para guardar con los datos enviados por POST
        form = AgregarPromo(instance=promo, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogapp:Promos')

    context = {
        'title': 'Edit',
        'subtitle': promo.descripcion,
        'form': form,
        'avatar': avatar,
    }
    return render(request, 'blogapp/edit_promo.html', context)


@login_required
def post_detail(request, post_id):
    """Display full post."""
    
    # Post que se va a mostrar
    post = Post.objects.get(id=post_id)

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''
    
    context = {
        'title': 'Detail',
        'subtitle': post.title,
        'avatar': avatar,
        'post': post
    }
    return render(request, 'blogapp/post_detail.html', context)


# Class Based Views

class DeletePromo(LoginRequiredMixin, DeleteView):
    model = Promo
    success_url = '/promos/'


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/pages/'


def about(request):
    """About context."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    context = {
        'avatar': avatar,
        'title': 'About',
        'message': 'Bienvenidos a City Travel',
        'subtitle': 'About'
        }
    return render(request, 'blogapp/about.html', context)