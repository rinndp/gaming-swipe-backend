from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

from favgames.models import Platform, FavGame
from favgames.serializers.create_favgame_serializer import CreateFavGameSerializer
from users.models import CustomUser

class AddFavGameView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, slug):
        data = request.data
        id_api = data.get('id_api')

        try:
            user = CustomUser.objects.get(slug=slug)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": f"User does not exist with slug: {slug}"},
                status=HTTP_400_BAD_REQUEST
            )

        if not FavGame.objects.filter(id_api=id_api).exists():
            serializer = CreateFavGameSerializer(data=request.data)

            if serializer.is_valid():
                fav_game = serializer.save()
                user.favorite_games.add(fav_game)

                return Response(
                    {"message": "FavGame created correctly"},
                    status=HTTP_201_CREATED
                )
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        else:
            fav_game = FavGame.objects.get(id_api=id_api)
            serializer = CreateFavGameSerializer(fav_game, data=request.data, partial=True)

            if serializer.is_valid():
                fav_game = serializer.save()

                if fav_game in user.favorite_games.all():
                    return Response(
                        {"message": f"This game is already in your favorite game"},
                        status=HTTP_200_OK
                    )

                user.favorite_games.add(fav_game)
                return Response(
                    {"message": "FavGame created correctly"},
                    status=HTTP_200_OK
                )

class AddPlayedGameView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, slug):
        data = request.data
        id_api = data.get('id_api')

        try:
            user = CustomUser.objects.get(slug=slug)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": f"User does not exist with slug: {slug}"},
                status=HTTP_400_BAD_REQUEST
            )

        fav_game = FavGame.objects.get(id_api=id_api)
        user.played_games.add(fav_game)
        user.favorite_games.remove(fav_game)
        return Response(
            {"message": "Game added correctly"},
            status=HTTP_200_OK
        )
