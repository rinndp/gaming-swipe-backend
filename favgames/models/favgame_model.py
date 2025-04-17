from django.db import models

from favgames.models.genre_model import Genre
from favgames.models.platform_model import Platform


class FavGame(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, verbose_name="Nombre")
    rating_score = models.FloatField(null=True, blank=True, default=0, verbose_name="Nota")
    release_year = models.IntegerField(null=True, blank=True, default=0, verbose_name="Año lanzamiento")
    image_url = models.URLField(null=True, blank=True, default="", verbose_name="URL de imagen")
    platforms = models.ManyToManyField(Platform, related_name="favgames", default=[], blank=True, verbose_name="Platformas")
    genres = models.ManyToManyField(Genre, related_name="favgames", default=[], blank=True, verbose_name="Genres")

    class Meta:
        db_table = "favgames"
        verbose_name = "Juego favorito"
        verbose_name_plural = "Juegos favoritos"

    def __str__(self):
        return self.name
