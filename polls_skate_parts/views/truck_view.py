from rest_framework import generics

from ..models.truck_model import Truck
from ..serializer.truck_serializer import TruckSerializer


class TruckList(generics.ListAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class TruckRetrieve(generics.RetrieveAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class TruckCreate(generics.CreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class TruckUpdate(generics.UpdateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class TruckDestroy(generics.DestroyAPIView):
    queryset = Truck.objects.all()
