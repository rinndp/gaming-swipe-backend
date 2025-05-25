from rest_framework import serializers
from rest_framework.authtoken.admin import User

from users.models import CustomUser

class SearchUserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = CustomUser
        fields = ('name', 'last_name', 'image', 'slug',)

class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = CustomUser
        fields = ('name', 'last_name', 'email', 'image',)

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'last_name', 'email', 'password')

    def validate (self, data):
        name = data.get('name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        if name is None:
            raise serializers.ValidationError('Users must have a name')

        if last_name is None:
            raise serializers.ValidationError('Users must have a last name')

        if len(password) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')

        return data


