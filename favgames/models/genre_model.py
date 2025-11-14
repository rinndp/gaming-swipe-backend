from django.db import models


class Genre(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, verbose_name='Genre')

    class Meta:
        db_table = 'genres'
        verbose_name = 'Genre'
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name