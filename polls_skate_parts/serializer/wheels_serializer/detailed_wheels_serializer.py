from rest_framework import serializers


class DetailedWheelsSerializer(serializers.ModelSerializer):
    id_wheels: int
    wheels_size: int
    wheels_brand: str
    wheels_color: str
