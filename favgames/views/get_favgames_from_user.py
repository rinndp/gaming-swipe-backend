from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from favgames.models import FavGame
from favgames.serializers.get_favgames_serializer import GetFavgamesSerializer
from users.models import CustomUser

class GetFavGamesFromUser(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, slug):
        try:
            user = CustomUser.objects.get(slug=slug)
        except CustomUser.DoesNotExist:
            return Response({"error":f"User not found with slug: {slug}"},status=HTTP_400_BAD_REQUEST)

        favgames = FavGame.objects.filter(favorited_by=user).all()
        serializer = GetFavgamesSerializer(favgames, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
