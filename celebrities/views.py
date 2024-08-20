from rest_framework import mixins
from rest_framework import generics
from .models import Celebrity
from .serializers import CelebritySerializer
from .filters import get_filtered_celebrities

class CelebrityList(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = CelebritySerializer

    def get_queryset(self):
        queryset = Celebrity.objects.all()
        query_params = self.request.query_params

        return get_filtered_celebrities(queryset, query_params)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
