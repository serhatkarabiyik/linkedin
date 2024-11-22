from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from posts.models import Post  

class Reaction(models.Model):
    REACTION_CHOICES = [
        ('like', 'J\'aime'),
        ('bravo', 'Bravo'),
        ('soutien', 'Soutien'),
        ('j_adore', 'J\'adore'),
        ('instructif', 'Instructif'),
        ('drôle', 'Drôle'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=20, choices=REACTION_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} - {self.reaction} - {self.post.id}"
