""" Urls patterns for users."""
from django.urls import path, include

from users.views import *

app_name = 'users'

urlpatterns = [
    # Django's defaults auth urls login/logout
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('signup/', register, name='register'),
]

