from django.db import models


class Platform(models.Model):
    abbreviation = models.CharField(unique=True, null=True, blank=True, verbose_name='abbreviation')
    name = models.CharField(null=False, blank=False, verbose_name='name', default="")

    class Meta:
        db_table = 'platforms'
        verbose_name = 'Platform'
        verbose_name_plural = 'Platforms'

    def __str__(self):
        return self.abbreviation or self.name