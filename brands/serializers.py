from rest_framework import serializers
from .models import Brand

class OutfitItemBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name"]
