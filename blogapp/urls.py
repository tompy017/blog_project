"""Url patterns for blog."""

from django.urls import path

from blogapp.views import *

app_name = 'blogapp'


urlpatterns = [
    # Inicio
    path('', inicio, name='Inicio'),
    # Promociones
    path('promos/', promos, name='Promos'),
    path('promos/new_promo/', agregar_promos, name='NewPromo'),
    path('promos/delete_promo/<promo_id>/', delete_promo, name='DeletePromo'),
    path('promos/edit_promo/<promo_id>/', edit_promo, name='EditPromo'),
    # Posts
    path('pages/', posts, name='Posts'),
    path('pages/new_post/', agregar_post, name='NewPost'),
    path('pages/delete_post/<post_id>/', delete_post, name='DeletePost'),
    path('pages/edit_post/<post_id>/', edit_post, name='EditPost'),
    path('pages/<pk>/', PostDetail.as_view(), name='PostDetail'),
]