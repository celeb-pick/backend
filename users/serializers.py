from rest_framework import serializers
from .models import CustomUser

class OutfitPostCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "profile_image_url",
            "nickname",
        ]
