from datetime import date

from rest_framework import serializers

from favgames.models import FavGame, Platform, Genre


class PlatformSerializer(serializers.ModelSerializer):
    abbreviation = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Platform
        fields = ('abbreviation', 'name',)
        extra_kwargs = {
            'abbreviation': {'validators': []},
            'name': {'validators': []}
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
    release_date = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = FavGame
        fields = ('name', 'rating_score', 'release_date', 'image_url', 'platforms', 'genres', 'id_api', 'summary')

    def validate (self, data):
        name = data.get('name')
        release_date_timestamp = data.get('release_date')

        if name is None:
            raise serializers.ValidationError('Name is required')

        if release_date_timestamp is not None:
            try:
                data['release_date'] = date.fromtimestamp(release_date_timestamp)
            except (ValueError, TypeError, OSError) as e:
                raise serializers.ValidationError({
                    'release_date': f'Invalid timestamp: {str(e)}'
                })

        return data

    def create(self, validated_data):
        genres_data = validated_data.pop('genres', [])
        platforms_data = validated_data.pop('platforms', [])

        fav_game = FavGame.objects.create(**validated_data)

        for genre in genres_data:
            genre, _ = Genre.objects.get_or_create(name=genre['name'])
            fav_game.genres.add(genre)

        for platform in platforms_data:
            platform, _ = Platform.objects.get_or_create(abbreviation=platform.get("abbreviation"), name=platform.get("name"))
            fav_game.platforms.add(platform)

        return fav_game

    def update(self, instance, validated_data):
        genres_data = validated_data.pop('genres', [])
        platforms_data = validated_data.pop('platforms', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if genres_data:
            instance.genres.clear()
            for genre in genres_data:
                genre, _ = Genre.objects.get_or_create(name=genre['name'])
                instance.genres.add(genre)

        if platforms_data:
            instance.platforms.clear()
            for platform in platforms_data:
                abbrev = (platform.get("abbreviation") or "").strip() or None
                name = (platform.get("name") or "").strip() or None

                platform_obj, created = Platform.objects.get_or_create(
                    abbreviation=abbrev,
                    defaults={'name': name},
                )

                if not created and name and not platform_obj.name:
                    platform_obj.name = name
                    platform_obj.save()

                instance.platforms.add(platform_obj)

        return instance