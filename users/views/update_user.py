import os

from django.views.generic import UpdateView
from rest_framework import status, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from users.models import CustomUser


class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, slug):
        data = request.data
        username = data.get("username")
        image = request.FILES.get("image")

        user = get_object_or_404(CustomUser, slug=slug)

        if username is not None:
            if len(username) > 30:
                return Response({"error": "Username cannot be longer than 30 characters"}, status=HTTP_400_BAD_REQUEST)
            if CustomUser.objects.filter(username=username).exists():
                return Response({"error": "Username already registered"}, status=HTTP_400_BAD_REQUEST)
            else:
                user.username = username
        if image is not None:
            if user.image and hasattr(user.image, 'path'):
                old_image_path = user.image.path
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)
            user.image = image

        user.save()
        return Response({"message":"User updated correctly"}, status=HTTP_200_OK)

class UpdatePasswordView (APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, slug):
        data = request.data
        password = data.get("oldPassword")
        new_password = data.get("newPassword")

        user = get_object_or_404(CustomUser, slug=slug)

        if len(new_password) < 8:
            return Response({"error":"New password must be at least 8 characters"}, status=HTTP_400_BAD_REQUEST)

        if user.check_password(password):
            user.set_password(new_password)
            user.save()
            return Response({"message":"Password updated correctly"}, status=HTTP_200_OK)
        else:
            return Response({"error":"Invalid password"}, status=HTTP_401_UNAUTHORIZED)


