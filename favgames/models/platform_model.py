from django.db import models


class Platform(models.Model):
    abbreviation = models.CharField(unique=True, null=False, blank=False, verbose_name='abbreviation')

    class Meta:
        db_table = 'platforms'
        verbose_name = 'Platform'
        verbose_name_plural = 'Platforms'

    def __str__(self):
        return self.abbreviation