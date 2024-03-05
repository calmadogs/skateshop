from rest_framework import generics

from ..models.bearing_model import Bearing
from ..serializers.bearing_serializer import BearingSerializer


class BearingList(generics.ListAPIView):
    queryset = Bearing.objects.all()
    serializer_class = BearingSerializer


class BearingRetrieve(generics.RetrieveAPIView):
    queryset = Bearing.objects.all()
    serializer_class = BearingSerializer


class BearingCreate(generics.CreateAPIView):
    queryset = Bearing.objects.all()
    serializer_class = BearingSerializer


class BearingUpdate(generics.UpdateAPIView):
    queryset = Bearing.objects.all()
    serializer_class = BearingSerializer


class BearingDestroy(generics.DestroyAPIView):
    queryset = Bearing.objects.all()
