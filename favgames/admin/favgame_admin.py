from django.contrib import admin

from favgames.models import FavGame, Platform, Genre


class FavGameAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'rating_score')
    search_fields = ('name',)
    readonly_fields = ('id_api', 'name', 'release_date', 'summary', 'image_url', 'platforms', 'genres', 'rating_score',)
    list_filter = ('platforms',)

admin.site.register(FavGame, FavGameAdmin)


class PlatformAdmin(admin.ModelAdmin):
    list_display = ("id", 'abbreviation', 'name',)
    search_fields = ('abbreviation', 'name',)
    readonly_fields = ('abbreviation', 'name')

admin.site.register(Platform, PlatformAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", 'name',)
    search_fields = ('name',)


admin.site.register(Genre, GenreAdmin)