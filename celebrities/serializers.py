from rest_framework import serializers
from .models import Celebrity

class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = [
            "id",
            "name",
            "profile_image_url",
        ]


class OutfitPostCelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = [
            "id",
            "name",
        ]
