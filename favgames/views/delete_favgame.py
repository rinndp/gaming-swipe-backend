from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from favgames.models import FavGame
from users.models import CustomUser

class DeleteFavGameView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, slug, id_api):
        try:
            user = CustomUser.objects.get(slug=slug)
        except CustomUser.DoesNotExist:
            return Response({
                "error": f"User not found with slug: {slug}"},
                status=HTTP_400_BAD_REQUEST)

        try:
            favgame = FavGame.objects.get(id_api=id_api)
            print(favgame)
        except IndexError:
            return Response({
                "error": f"Game not found with id_api: {id_api}"},
                status=HTTP_400_BAD_REQUEST)


        if user.favorite_games.filter(id=favgame.id).exists():
            user.favorite_games.remove(favgame)
            return Response({"message": "Game deleted correctly"}, status=HTTP_200_OK)
        else:
            return Response({"error": "Game not in user's favorite games list"}, status=HTTP_400_BAD_REQUEST)

class DeletePlayedGameView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, slug, id_api):
        try:
            user = CustomUser.objects.get(slug=slug)
        except CustomUser.DoesNotExist:
            return Response({
                "error": f"User not found with slug: {slug}"},
                status=HTTP_400_BAD_REQUEST)

        try:
            favgame = FavGame.objects.get(id_api=id_api)
            print(favgame)
        except IndexError:
            return Response({
                "error": f"Game not found with id_api: {id_api}"},
                status=HTTP_400_BAD_REQUEST)

        if user.played_games.filter(id=favgame.id).exists():
            user.played_games.remove(favgame)
            return Response({"message": "Game deleted correctly"}, status=HTTP_200_OK)
        else:
            return Response({"error": "Game not in user's favorite games list"}, status=HTTP_400_BAD_REQUEST)