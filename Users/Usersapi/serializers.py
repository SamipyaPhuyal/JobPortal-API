
from Users.models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Count

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
        
class UserProfileSerializer(serializers.ModelSerializer):
    user=serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = UserProfile
        fields ="__all__"
        
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    type = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "password", "password2","type", "email"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email")
        )

        UserProfile.objects.create(
            user=user,
            type=validated_data["type"]
        )
        return user
        