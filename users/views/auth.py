from rest_framework import permissions
from rest_framework.permissions import AllowAny
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
        google_id= data.get('google_id')

        if email is None:
            return Response({"error": 'Email is required'}, status=HTTP_401_UNAUTHORIZED)

        if google_id and password is None:
            try:
                user = CustomUser.objects.get(email=email, google_id=google_id)
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                return Response({
                    "slug": user.slug,
                    "access_token": str(access_token),
                    "refresh_token": str(refresh),
                }, status=HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return Response({"error": 'User does not exist with google_id: '+google_id}, status=HTTP_400_BAD_REQUEST)

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
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        google_id = data.get('google_id')

        serializer = RegisterUserSerializer(data=data)
        if CustomUser.objects.filter(email=email).exists():
            return Response({"error": "Email already registered"}, status=HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            CustomUser.objects.create_user(email=email, password=password, username=username, google_id=google_id)
            return Response({"message": "User created successfully"}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class CheckIfEmailIsAlreadyRegistered(APIView):
    permissions_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get('email')

        if email is None:
            return Response({"error": "Email is required"}, status=HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(email=email).exists():
            return Response({"error": "Email already registered"}, status=HTTP_400_BAD_REQUEST)

        return Response({"message": "Email not registered"}, status=HTTP_200_OK)


