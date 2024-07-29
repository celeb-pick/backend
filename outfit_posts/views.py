from rest_framework import mixins
from rest_framework import generics
from .models import OutfitPost
from .serializers import OutfitPostSerializer

class OutfitPostList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = OutfitPost.objects.all()
    serializer_class = OutfitPostSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        
        return context

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
