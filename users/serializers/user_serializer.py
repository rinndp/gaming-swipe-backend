from rest_framework import serializers
from rest_framework.authtoken.admin import User

from users.models import CustomUser

class SearchUserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'image', 'slug',)

class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'image',)

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, allow_blank=True, write_only=True)
    google_id = serializers.CharField(required=False, allow_blank=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'google_id')

    def validate (self, data):
        name = data.get('username')
        google_id = data.get('google_id')
        password = data.get('password')

        if name is None:
            raise serializers.ValidationError('Users must have a name')

        if password is None and google_id is None:
            raise serializers.ValidationError('User logged with Google must have a google_id')

        if len(name) > 20:
            raise serializers.ValidationError('Name cannot be longer than 20 characters')

        if password and len(password) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')


        return data


