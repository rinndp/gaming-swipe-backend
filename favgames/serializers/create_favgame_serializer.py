from rest_framework import serializers

from favgames.models import FavGame, Platform, Genre


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('abbreviation',)
        extra_kwargs = {
            'abbreviation': {'validators': []}
        }

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)
        extra_kwargs = {
            'name': {'validators': []}
        }

class CreateFavGameSerializer(serializers.ModelSerializer):
    platforms = PlatformSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = FavGame
        fields = ('name', 'rating_score', 'release_year', 'image_url', 'platforms', 'genres',)

    def validate (self, data):
        name = data.get('name')

        if name is None:
            raise serializers.ValidationError('Name is required')

        return data

    def create(self, validated_data):
        genres_data = validated_data.pop('genres', [])
        platforms_data = validated_data.pop('platforms', [])
        fav_game = FavGame.objects.create(**validated_data)

        for genre in genres_data:
            genre, _ = Genre.objects.get_or_create(name=genre['name'])
            fav_game.genres.add(genre)

        for platform in platforms_data:
            platform, _ = Platform.objects.get_or_create(abbreviation=platform['abbreviation'])
            fav_game.platforms.add(platform)

        return fav_game