from rest_framework import generics

from ..models.shape_model import Shape
from ..serializer.shape_serializer.detailed_shape_serializer import DetailedShapeSerializer


class ShapeList(generics.ListAPIView):
    queryset = Shape.objects.all()
    serializer_class = DetailedShapeSerializer
