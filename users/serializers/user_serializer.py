from rest_framework import serializers
from rest_framework.authtoken.admin import User

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

