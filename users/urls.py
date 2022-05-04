""" Urls patterns for users."""
from django.urls import path, include

from users.views import *

app_name = 'users'


urlpatterns = [
    # Django's defaults auth urls login/logout
    path('', include('django.contrib.auth.urls')),
    # Messages
    # path('messages/', messages, name='Messages'),
    # path('messages/delete/<msg_id>/', delete_msg, name='DeleteMsg'),
    # path('messages/new_msg/', new_message, name='NewMsg'),
    # Registration/Modification patterns
    path('signup/', register, name='register'),
    path('update/', update_profile, name='UpdateProfile'),
    path('update/avatar/', update_avatar, name='UpdateAvatar'),
    path('profile/<user_id>/', profile, name='Profile'),
]

