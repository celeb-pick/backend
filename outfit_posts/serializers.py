from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import OutfitPost, OutfitItem
from brands.serializers import OutfitItemBrandSerializer
from users.serializers import OutfitPostCreatorSerializer
from celebrities.serializers import OutfitPostCelebritySerializer
from users.models import CustomUser
from celebrities.models import Celebrity
from brands.models import Brand

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
            "image",
            *BaseOutfitSerializer.Meta.fields,
            "brand",
        ]

class OutfitPostSerializer(BaseOutfitSerializer, serializers.ModelSerializer):
    celebrity = OutfitPostCelebritySerializer(read_only=True)
    creator = OutfitPostCreatorSerializer(read_only=True)
    items = TinyOutfitItemSerializer(many=True, read_only=True)

    celebrity_id = serializers.IntegerField(min_value=1, write_only=True)
    item_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        write_only=True,
        allow_empty=False
    )

    class Meta:
        model = OutfitPost
        fields = [
            "id",
            "title",
            "created_at",
            "gender",
            "image",
            *BaseOutfitSerializer.Meta.fields,
            "celebrity",
            "creator",
            "items",
            
            # write onlys
            "celebrity_id",
            "item_ids",
        ]

    def validate_celebrity_id(self, value):
        celebrity = Celebrity.objects.filter(id=value).first()
        if not celebrity:
            raise serializers.ValidationError("올바르지 않은 셀럽 id값 입니다.")
        
        return value

    def validate_item_ids(self, value):
        if len(value) > 5:
            raise serializers.ValidationError("코디 아이템은 5개 이하여야 합니다.")

        items_count = OutfitItem.objects.filter(id__in=value).count()
        if len(value) != items_count:
            raise serializers.ValidationError("올바르지 않은 코디 아이템 id값이 포함되어 있습니다.")
        
        return value

    def create(self, validated_data):
        request = self.context['request']

        item_ids = validated_data.pop('item_ids')
        items = OutfitItem.objects.filter(id__in=item_ids)

        celebrity_id = validated_data.pop('celebrity_id')
        celebrity = Celebrity.objects.get(id=celebrity_id)

        outfit_post = OutfitPost.objects.create(**validated_data, celebrity=celebrity, creator=request.user)
        outfit_post.items.set(items)
        
        return outfit_post


class OutfitItemSerializer(BaseOutfitSerializer, serializers.ModelSerializer):
    brand = OutfitItemBrandSerializer(read_only=True)
    brand_name = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = OutfitItem
        fields = [
            "id",
            "category",
            "name",
            "purchase_link",
            "image",
            *BaseOutfitSerializer.Meta.fields,
            "brand",

            # write onlys
            "brand_name",
        ]

    def create(self, validated_data):
        brand_name = validated_data.pop('brand_name')
        brand = Brand.objects.get_or_create(name=brand_name)[0]

        outfit_item = OutfitItem.objects.create(**validated_data, brand=brand)
        
        return outfit_item
