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
        name = data.get('name')
        last_name = data.get('last_name')

        if name is None and last_name is None:
            return Response({}, status=HTTP_200_OK)

        if last_name is None:
            users = CustomUser.objects.filter(
                Q(name__icontains=name) | Q(last_name__icontains=name)
            )
        else:
            users = CustomUser.objects.filter(name__icontains=name, last_name__icontains=last_name)

        serializer = SearchUserSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

