from rest_framework import serializers
from .models import Celebrity

class OutfitPostCelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = [
            "id",
            "name",
        ]
