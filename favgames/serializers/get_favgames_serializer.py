from rest_framework import serializers
from favgames.models import FavGame

class GetFavgamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavGame
        fields = ('id', 'name', 'image_url', 'id_api',)