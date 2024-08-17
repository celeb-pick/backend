from rest_framework import serializers
from .models import OutfitPost, OutfitItem
from brands.serializers import OutfitItemBrandSerializer
from users.serializers import OutfitPostCreatorSerializer
from celebrities.serializers import OutfitPostCelebritySerializer
from users.models import CustomUser

class BaseOutfitSerializer(serializers.Serializer):
    scrap_count = serializers.SerializerMethodField()
    is_scrapped = serializers.SerializerMethodField()

    class Meta:
        abstract = True
        fields = [
            "scrap_count",
            "is_scrapped",
        ]

    def get_scrap_count(self, obj):
        return obj.scraps.count()

    def get_is_scrapped(self, obj):
        user = self.context["request"].user
        if user.is_anonymous:
            return None

        if not obj.scraps.filter(user=user).exists():
            return False

        return True

class TinyOutfitItemSerializer(BaseOutfitSerializer, serializers.ModelSerializer):
    brand = OutfitItemBrandSerializer()

    class Meta:
        model = OutfitItem
        fields = [
            "id",
            "name",
            "purchase_link",
            "image_url",
            *BaseOutfitSerializer.Meta.fields,
            "brand",
        ]

class OutfitPostSerializer(BaseOutfitSerializer, serializers.ModelSerializer):
    celebrity = OutfitPostCelebritySerializer()
    creator = OutfitPostCreatorSerializer()
    items = TinyOutfitItemSerializer(many=True)

    class Meta:
        model = OutfitPost
        fields = [
            "id",
            "title",
            "created_at",
            "gender",
            "image_url",
            *BaseOutfitSerializer.Meta.fields,
            "celebrity",
            "creator",
            "items",
        ]


class OutfitItemSerializer(BaseOutfitSerializer, serializers.ModelSerializer):
    brand = OutfitItemBrandSerializer()

    class Meta:
        model = OutfitItem
        fields = [
            "id",
            "category",
            "name",
            "purchase_link",
            "image_url",
            *BaseOutfitSerializer.Meta.fields,
            "brand",
        ]
