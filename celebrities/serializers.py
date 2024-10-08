from rest_framework import serializers
from .models import Celebrity

class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = [
            "id",
            "name",
            "category",
            "profile_image"
        ]


class OutfitPostCelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = [
            "id",
            "name",
        ]
