from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    """Avatar for users."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user}"

