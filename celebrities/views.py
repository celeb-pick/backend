from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics
from .models import Celebrity
from .serializers import CelebritySerializer
from .filters import get_filtered_celebrities

class CelebrityList(mixins.ListModelMixin,  mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = CelebritySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Celebrity.objects.all()
        query_params = self.request.query_params

        return get_filtered_celebrities(queryset, query_params)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        
        return context

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
