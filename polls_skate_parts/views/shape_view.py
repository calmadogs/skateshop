from rest_framework import generics

from ..serializers.shape_serializer import ShapeSerializer
from ..models.shape_model import Shape


class ShapeList(generics.ListAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer


class ShapeRetrieve(generics.RetrieveAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer


class ShapeCreate(generics.CreateAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer


class ShapeUpdate(generics.UpdateAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer


class ShapeDestroy(generics.DestroyAPIView):
    queryset = Shape.objects.all()
