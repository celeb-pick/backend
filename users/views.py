from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from outfit_posts.serializers import OutfitPostSerializer, OutfitItemSerializer
from outfit_posts.models import OutfitPost
from outfit_posts.filters import get_filtered_outfit_posts
from users.models import CustomUser

class MyOutfitPostScrapList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OutfitPostSerializer

    def get_queryset(self):
        queryset = self.request.user.outfit_post_scraps.all().order_by("-scraps__created_at")
        query_params = self.request.query_params

        return get_filtered_outfit_posts(queryset, query_params)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        
        return context

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MyOutfitItemScrapList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OutfitItemSerializer

    def get_queryset(self):
        queryset = self.request.user.outfit_item_scraps.all().order_by("-scraps__created_at")

        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        
        return context

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
