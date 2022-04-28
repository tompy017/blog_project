"""Models for Usersapp (Avatar and Message)."""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Avatar(models.Model):
    """Avatar for users."""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user}"


class Message(models.Model):
    """DMs for users."""
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    msg = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self) -> str:
        return f"{self.msg[:50]}[...]"
