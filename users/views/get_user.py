from django.views import View
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from users.models import CustomUser
from users.serializers import UserSerializer


class GetUserView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, slug):
        try:
            user = CustomUser.objects.get(slug=slug)
        except CustomUser.DoesNotExist:
            return Response({"error":f"User not found with slug: {slug}"},status=HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)

