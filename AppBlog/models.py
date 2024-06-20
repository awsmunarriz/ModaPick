from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    def __str__(self):
        return self.title


class Favoritos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posteo = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta():
        unique_together = ('user', 'posteo')
        verbose_name = 'Favoritos'
        verbose_name_plural = 'Favoritos'

    def __str__(self):
        return f'{self.user.username} - {self.posteo.title}'
