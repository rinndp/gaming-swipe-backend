from django.contrib import admin

from favgames.models import FavGame, Platform, Genre


class FavGameAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'rating_score')
    search_fields = ('name',)

    list_filter = ('platforms',)

admin.site.register(FavGame, FavGameAdmin)


class PlatformAdmin(admin.ModelAdmin):
    list_display = ("id", 'abbreviation',)
    search_fields = ('abbreviation',)

admin.site.register(Platform, PlatformAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", 'name',)
    search_fields = ('name',)


admin.site.register(Genre, GenreAdmin)