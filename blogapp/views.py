
from django.shortcuts import render, redirect

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


def agregar_promos(request):
    """View to add new promotions."""

    if request.method != 'POST':
        # Paso formulario vacio
        form = AgregarPromo()

        context = {
            'form': form,
            'title': 'Agregar Promo',
        }
        return render(request, 'blogapp/new_promo.html', context)

    else:
        # Traigo las promos para renderizarlas
        promos = Promo.objects.all()

        # Paso formulario con datos ingresados por POST
        form = AgregarPromo(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'promos': promos,
                'title': 'Promos',
                'subtitle': '¡Mira las promociones que hay para tu viaje!',
                'search': 'Buscar por categoría (ej: "Alojamiento")',
                'added': 'Promo agregada correctamente',

            }
            return render(request, 'blogapp/promos.html', context)


def agregar_post(request):
    """View to add new posts."""

    if request.method != 'POST':
        # Paso formulario vacio
        form = NuevoPost()

        context = {
            'form': form, 
            'title': 'Nuevo Post',
        }
        return render(request, 'blogapp/new_post.html', context)
    
    else:
        # Traigo todos los posts para renderizarlos
        posts = Post.objects.order_by('-date_added')
        
        # Paso formulario con datos ingresados por POST
        form = NuevoPost(request.POST)
        if form.is_valid():
            form.save()

            context = {
                'posts': posts,
                'title': 'Posts',
                'subtitle': '¡El listado completo de nuestros posts!',
                'search': 'Buscar por ciudad',
                'added': 'Post agregado correctamente',
            }
            return render(request, 'blogapp/posts.html', context)
    

def delete_post(request, post_id):
    """View for deleting posts."""
    # Para que renderize nuevamente los posts que quedaron luego de borrar (de mas nuevo a mas antiguo)
    posts = Post.objects.order_by('-date_added')

    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        context = {
            'title': 'Posts',
            'search': 'Buscar por ciudad',
            'subtitle': '¡El listado completo de nuestros posts!',
            'deleted': 'Post eliminado correctamente',
            'posts': posts,
        }

        return render(request, 'blogapp/posts.html', context)

    except Exception as exc:
        return render(request, 'blogapp/index.html')
    

def delete_promo(request, promo_id):
    """View for deleting promos."""

    # Para que renderize nuevamente los posts que quedaron luego de borrar.
    promos = Promo.objects.all()

    # Try para buscar promo por id
    try:
        promo = Promo.objects.get(id=promo_id)
        promo.delete()
        context = {
            'title': 'Promos',
            'subtitle': '¡Mira las promociones que hay para tu viaje!',
            'deleted': 'Promo eliminada correctamente',
            'search': 'Buscar por categoría (ej: "Alojamiento")',
            'promos': promos,
        }
        return render(request, 'blogapp/promos.html', context)

    # Si levanta una excepcion renderiza a la pagina de inicio
    except Exception as exc:
        return render(request, 'blogapp/index.html')


def edit_post(request, post_id):
    """Edit an existing post."""
    # Post que se va a editar
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # Formulario ya poblado con los datos a editar
        form = NuevoPost(instance=post)

        context = {
            'title': 'Edit',
            'subtitle': post.title,
            'form': form,
        }
        return render(request, 'blogapp/edit_post.html', context)
    
    else:
        # Todos los posts para renderizarlos por medio del context
        posts = Post.objects.order_by('-date_added')
        # Formulario para guardar
        form = NuevoPost(instance=post, data=request.POST)

        if form.is_valid():
            form.save()

            context = {
                'title': 'Posts',
                'search': 'Buscar por ciudad',
                'subtitle': '¡El listado completo de nuestros posts!',
                'edited': 'Entrada editada correctamente.',
                'posts': posts,
            }
            return render(request, 'blogapp/posts.html', context)
    

def edit_promo(request, promo_id):
    """Edit an existing promo."""
    
    # Promocion a editar
    promo = Promo.objects.get(id=promo_id)

    if request.method != 'POST':
        # Formulario ya poblado con datos a editar
        form = AgregarPromo(instance=promo)

        context = {
            'title': 'Edit',
            'subtitle': promo.descripcion,
            'form': form,
        }
        return render(request, 'blogapp/edit_promo.html', context)
    
    else:
        # Traigo todas las promos para liostarlas en contexto y renderizarlas
        promos = Promo.objects.all()
        # Formulario para guardar
        form = AgregarPromo(instance=promo, data=request.POST)

        if form.is_valid():
            form.save()

            context = {
                'title': 'Promos',
                'search': 'Buscar por categoría (ej: "Alojamiento")',
                'subtitle': '¡Mira las promociones que hay para tu viaje!',
                'edited': 'Entrada editada correctamente.',
                'promos': promos,
            }
            return render(request, 'blogapp/promos.html', context)