from django.contrib import admin

from users.models import Avatar, Message

# Register your models here.
admin.site.register(Avatar)
admin.site.register(Message)