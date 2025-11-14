from django.db.models import Q
from django.views import View
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from users.models import CustomUser
from users.serializers import UserSerializer, SearchUserSerializer


class GetUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, slug):
        try:
            user = CustomUser.objects.get(slug=slug)
        except CustomUser.DoesNotExist:
            return Response({"error":f"User not found with slug: {slug}"},status=HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)


class SearchUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        username = data.get('username')

        if username is None:
            return Response({}, status=HTTP_200_OK)


        users = CustomUser.objects.filter(username__icontains=username)

        serializer = SearchUserSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

