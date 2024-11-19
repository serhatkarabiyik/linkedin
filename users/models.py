from django.db import models
from django.contrib.auth.models import User as AuthUser

class Profile(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    picture = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profil de {self.user.username}"

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"
        ordering = ['-created_at']
