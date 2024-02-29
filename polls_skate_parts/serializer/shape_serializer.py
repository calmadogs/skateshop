from rest_framework import serializers

from ..models.shape_model import Shape


class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = "__all__"
