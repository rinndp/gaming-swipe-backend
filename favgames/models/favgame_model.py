from django.db import models

from favgames.models.genre_model import Genre
from favgames.models.platform_model import Platform


class FavGame(models.Model):
    name = models.CharField(null=False, blank=False, unique=False, verbose_name="Name")
    rating_score = models.FloatField(null=True, blank=True, default=0, verbose_name="Rating")
    release_date = models.DateField(null=True, blank=True, verbose_name="Release Date")
    image_url = models.URLField(null=True, blank=True, default="", verbose_name="Image URL")
    summary = models.TextField(null=True, blank=True, default="", verbose_name="Summary")
    platforms = models.ManyToManyField(Platform, related_name="favgames", default=[], blank=True, verbose_name="Platforms")
    genres = models.ManyToManyField(Genre, related_name="favgames", default=[], blank=True, verbose_name="Genres")
    id_api = models.IntegerField(null=False, blank=False, default=0, verbose_name="ID API")

    class Meta:
        db_table = "favgames"
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        return self.name
