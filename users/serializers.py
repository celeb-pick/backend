from rest_framework import serializers
from .models import CustomUser

class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "nickname",
            "gender",
            "profile_image",
        ]

class OutfitPostCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "profile_image",
            "nickname",
        ]
