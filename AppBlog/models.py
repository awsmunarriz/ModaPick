from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    def __str__(self):
        return self.title


class Favoritos(models.Model):
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'

    INTERACTION_CHOICES = [
        (LIKE, _('Like')),
        (DISLIKE, _('Dislike')),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posteo = models.ForeignKey(Post, on_delete=models.CASCADE)
    interaction = models.CharField(_('Interaction'), max_length=7, choices=INTERACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'posteo', 'interaction')
        verbose_name = _('Favoritos')
        verbose_name_plural = _('Favoritos')

    def __str__(self):
        return f'{self.user.username} - {self.posteo.title} ({self.interaction})'
