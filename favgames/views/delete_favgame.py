from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from favgames.models import FavGame
from users.models import CustomUser

class DeleteFavGameView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, slug, position):
        data = request.data

        try:
            user = CustomUser.objects.get(slug=slug)
        except CustomUser.DoesNotExist:
            return Response({
                "error": f"User not found with slug: {slug}"},
                status=HTTP_400_BAD_REQUEST)

        try:
            favgame = user.favorite_games.all()[position]
            print(favgame)
        except IndexError:
            return Response({
                "error": f"FavGame not found with position: {position}"},
                status=HTTP_400_BAD_REQUEST)


        if user.favorite_games.filter(id=favgame.id).exists():
            user.favorite_games.remove(favgame)
            return Response({"message": "Game deleted correctly"}, status=HTTP_200_OK)
        else:
            return Response({"error": "FavGame not in user's favorite games list"}, status=HTTP_400_BAD_REQUEST)
