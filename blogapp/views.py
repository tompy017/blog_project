
from django.shortcuts import render, redirect
# CBV (class based views)
from django.views.generic.detail import DetailView
# Decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin # For loguin required of a class

# My models and forms
from blogapp.models import Post, Promo
from blogapp.forms import NuevoPost, AgregarPromo

# Create your views here.
def inicio(request):
    """Home page for blogapp."""

    context = {
        'title': 'Inicio',
        'message': 'Bienvenidos a City Travel',
        'subtitle': '¿Planificando tu próximo viaje? '
            'Lee las recomendaciones realizadas por los propios miembros del blog!',
    }
    return render(request, 'blogapp/index.html', context)


def promos(request):
    """View for promotions page."""
    # Defino variable conteniendo todas las promociones
    promos = Promo.objects.all()

    # Buscar promos por categoria
    category = request.GET.get('categoria')

    if category:
        promos = Promo.objects.filter(categoria__icontains=category)
        context = {
            'title': 'Promos',
            'category': category,
            'search': 'Buscar por categoría (ej: "Alojamiento")',
            'promos': promos,
        }
        return render(request, 'blogapp/promos.html', context)

    else:
        # Listar todas las promociones
        context = {
            'promos': promos,
            'title': 'Promos',
            'subtitle': '¡Mira las promociones que hay para tu viaje!',
            'search': 'Buscar por categoría (ej: "Alojamiento")',
        }
        return render(request, 'blogapp/promos.html', context)


def posts(request):
    """View for posts page."""
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
            'posts': posts
        }
        return render(request, 'blogapp/posts.html', context)
    
    else:
        # Listar todos los posts
        context = {
            'posts': posts,
            'title': 'Posts',
            'subtitle': '¡El listado completo de nuestros posts!',
            'search': 'Buscar por ciudad'
        }
        return render(request, 'blogapp/posts.html', context)

@login_required
def agregar_promos(request):
    """View to add new promotions."""

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = AgregarPromo()

    else:
        # Data submitted. Paso formulario con datos ingresados por POST
        form = AgregarPromo(request.POST)

        if form.is_valid():
            form.save()
            # Save y vuelve a promos
            return redirect('blogapp:Promos')

    context = {
        'form': form,
        'title': 'Agregar Promo',
    }
    return render(request, 'blogapp/new_promo.html', context)

@login_required
def agregar_post(request):
    """View to add new posts."""

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
    }
    return render(request, 'blogapp/new_post.html', context)

@login_required
def delete_post(request, post_id):
    """View for deleting posts."""
    # Try para obtener post por medio de su id con metodo get 
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return redirect('blogapp:Posts')
    # Si levanta una excepcion ya que no obtuvo registro
    except Exception as exc:
        return redirect('blogapp:Inicio')
    
@login_required
def delete_promo(request, promo_id):
    """View for deleting promos."""
    # Try para buscar promo por id
    try:
        promo = Promo.objects.get(id=promo_id)
        promo.delete()
        return redirect('blogapp:Promos')
    # Si levanta una excepcion renderiza a la pagina de inicio
    except Exception as exc:
        return redirect('blogapp:Inicio')

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
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
    }
    return render(request, 'blogapp/edit_post.html', context)
    
@login_required
def edit_promo(request, promo_id):
    """Edit an existing promo."""
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
    }
    return render(request, 'blogapp/edit_promo.html', context)


# Django's Class Based Views
# Como es una clase no funciona el @loguin_required. Se usa LoguinRequiredMixin)
class PostDetail(LoginRequiredMixin, DetailView):
    """CBV for post detail view."""
    # Model de donde hereda
    model = Post
    # Ubicacion del template
    template = "blogapp/post_detail.html"
    