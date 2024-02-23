from rest_framework import serializers


class UpdateShapeSerializer(serializers.ModelSerializer):
    shape_size: float
    shape_brand: str
    maple_or_marfin: str
