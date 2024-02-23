from rest_framework import serializers


class DetailedBearingSerializer(serializers.ModelSerializer):
    id_bearing: int
    bearing_brand: str
