from django.db import models


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    number_of_songs = models.IntegerField(default=0)

    def __str__(self):
        return self.name