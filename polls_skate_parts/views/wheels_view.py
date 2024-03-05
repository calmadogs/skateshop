from rest_framework import generics

from ..models.wheels_model import Wheels
from ..serializers.wheels_serializer import WheelsSerializer


class WheelsList(generics.ListAPIView):
    queryset = Wheels.objects.all()
    serializer_class = WheelsSerializer


class WheelsRetrieve(generics.RetrieveAPIView):
    queryset = Wheels.objects.all()
    serializer_class = WheelsSerializer


class WheelsCreate(generics.CreateAPIView):
    queryset = Wheels.objects.all()
    serializer_class = WheelsSerializer


class WheelsUpdate(generics.UpdateAPIView):
    queryset = Wheels.objects.all()
    serializer_class = WheelsSerializer


class WheelsDestroy(generics.DestroyAPIView):
    queryset = Wheels.objects.all()
