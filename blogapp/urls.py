"""Url patterns for blogapp."""

from django.urls import path

from blogapp.views import *

app_name = 'blogapp'


urlpatterns = [
    path('', inicio, name='Inicio'),
    # Promociones
    path('promos/', promos, name='Promos'),
    path('new_promo/', agregar_promos, name='NewPromo'),
    path('delete_promo/<promo_id>/', delete_promo, name='DeletePromo'),
    path('edit_promo/<promo_id>/', edit_promo, name='EditPromo'),
    # Posts
    path('posts/', posts, name='Posts'),
    path('new_post/', agregar_post, name='NewPost'),
    path('delete_post/<post_id>/', delete_post, name='DeletePost'),
    path('edit_post/<post_id>/', edit_post, name='EditPost'),
    path('post_detail/<pk>/', PostDetail.as_view(), name='PostDetail'),
]