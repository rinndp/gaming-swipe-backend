from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import CustomUser
from users.serializers import RegisterUserSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if email is None or password is None:
            return Response({"error": 'Email and password are required'}, status=HTTP_401_UNAUTHORIZED)

        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                return Response({
                    "slug": user.slug,
                    "access_token": str(access_token),
                    "refresh_token": str(refresh),
                }, status=HTTP_200_OK)
            else:
                return Response({"error": 'Invalid password'}, status=HTTP_401_UNAUTHORIZED)
        except CustomUser.DoesNotExist:
            return Response({"error": 'Email not found'}, status=HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        name = data.get('name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        serializer = RegisterUserSerializer(data=data)
        if serializer.is_valid():
            CustomUser.objects.create_user(email=email, password=password, name=name, last_name=last_name)
            return Response({"message": "User created successfully"}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




