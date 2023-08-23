from django.db import models
from django.contrib.auth.models import AbstractUser


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=150)
    duration = models.DurationField(blank=True, null=True)
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class User(AbstractUser):
    pass 
