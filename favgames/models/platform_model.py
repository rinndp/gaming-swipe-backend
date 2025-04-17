from django.db import models


class Platform(models.Model):
    abbreviation = models.CharField(unique=True, null=False, blank=False, verbose_name='Nombre')

    class Meta:
        db_table = 'platforms'
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'

    def __str__(self):
        return self.abbreviation