from django.db import models


class Genre(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, verbose_name='Género')

    class Meta:
        db_table = 'genres'
        verbose_name = 'Género'
        verbose_name_plural = "Géneros"

    def __str__(self):
        return self.name