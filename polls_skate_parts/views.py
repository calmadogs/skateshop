from rest_framework import generics
from .models import SkateParts
from .serializer import SkatePartsSerializer


class SkatePartsListView(generics.ListAPIView):
    """
    To display details of multiple objects.
    """
    queryset = SkateParts.objects.all()
    serializer_class = SkatePartsSerializer
