from rest_framework import generics
from .models import Hike
from .serializers import HikeSerializer


class HikeListView(generics.ListAPIView):
    """Список всех походов."""
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer


class HikeDetailView(generics.RetrieveAPIView):
    """Детали одного похода."""
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
