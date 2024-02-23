from rest_framework import serializers


class DetailedShapeSerializer(serializers.ModelSerializer):
    id_shape: int
    shape_size: float
    shape_brand: str
    maple_or_marfin: str
