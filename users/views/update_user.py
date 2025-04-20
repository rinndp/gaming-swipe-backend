from django.views.generic import UpdateView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from users.models import CustomUser


class UpdateUserView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, slug):
        data = request.data
        name = data.get("name")
        last_name = data.get("last_name")
        image = data.get("image")

        user = get_object_or_404(CustomUser, slug=slug)

        if name is not None:
            user.name = name
        if last_name is not None:
            user.last_name = last_name
        if image is not None:
            user.image = image

        user.save()
        return Response({"message":"User updated correctly"}, status=HTTP_200_OK)

