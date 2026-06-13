from django.db import models

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    is_public = models.BooleanField(default=False)
    saves_count = models.IntegerField(default=1)
    musics_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    is_public = models.BooleanField(default=False)
    playlist = models.ManyToManyField(Playlist, blank=True)
    favourites_count = models.IntegerField(default=1)
    listens_count = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    lyrics = models.TextField(default=0)
    source = models.CharField(max_length=500, blank=True, null=True)
    music_data = models.FileField(upload_to='musics/', blank=True)

    def __str__(self):
        return self.name