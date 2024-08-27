from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from .models import OutfitPost, OutfitItem
from .serializers import OutfitPostSerializer, OutfitItemSerializer
from .filters import get_filtered_outfit_posts, get_filtered_outfit_items

class OutfitPostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = OutfitPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = OutfitPost.objects.all()
        query_params = self.request.query_params

        return get_filtered_outfit_posts(queryset, query_params)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        
        return context

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OutfitItemList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = OutfitItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = OutfitItem.objects.all()
        query_params = self.request.query_params

        return get_filtered_outfit_items(queryset, query_params)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        
        return context

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
