from django.views.generic import CreateView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from favgames.models import Platform, FavGame
from favgames.serializers.create_favgame_serializer import CreateFavGameSerializer
from users.models import CustomUser

class CreateFavGameView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, slug):
        data = request.data
        name = data.get('name')

        try:
            user = CustomUser.objects.get(slug=slug)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": f"User does not exist with slug: {slug}"},
                status=HTTP_400_BAD_REQUEST
            )

        if not FavGame.objects.filter(name=name).exists():
            serializer = CreateFavGameSerializer(data=request.data)

            if serializer.is_valid():
                fav_game = serializer.save()
                user.favorite_games.add(fav_game)

                return Response(
                    {"message": "FavGame created correctly"},
                    status=HTTP_200_OK
                )
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        else:
            fav_game = FavGame.objects.get(name=name)
            user.favorite_games.add(fav_game)

            return Response(
                {"message": "FavGame created correctly"},
                status=HTTP_200_OK
            )
